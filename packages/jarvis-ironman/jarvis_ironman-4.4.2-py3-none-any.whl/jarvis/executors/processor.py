import os
import shutil
import warnings
from datetime import datetime
from multiprocessing import Process
from threading import Thread
from typing import Dict, List, Union

import psutil

from jarvis.api.server import jarvis_api
from jarvis.executors import crontab, offline, process_map, telegram
from jarvis.modules.audio import speech_synthesis
from jarvis.modules.database import database
from jarvis.modules.logger import logger
from jarvis.modules.microphone import graph_mic
from jarvis.modules.models import models
from jarvis.modules.retry import retry
from jarvis.modules.utils import shared, support, util

db = database.Database(database=models.fileio.base_db)


@retry.retry(attempts=3, interval=2, warn=True)
def delete_db() -> None:
    """Delete base db if exists. Called upon restart or shut down."""
    if os.path.isfile(models.fileio.base_db):
        logger.info("Removing %s", models.fileio.base_db)
        os.remove(models.fileio.base_db)
    if os.path.isfile(models.fileio.base_db):
        raise FileExistsError(f"{models.fileio.base_db} still exists!")
    return


def clear_db() -> None:
    """Deletes entries from all databases except for the tables assigned to hold data forever."""
    with db.connection:
        cursor = db.connection.cursor()
        for table, column in models.TABLES.items():
            if table in models.KEEP_TABLES:
                continue
            # Use f-string or %s as table names cannot be parametrized
            data = cursor.execute(f'SELECT * FROM {table}').fetchall()
            logger.info("Deleting data from %s: %s", table, util.matrix_to_flat_list([list(filter(None, d))
                                                                                      for d in data if any(d)]))
            cursor.execute(f"DELETE FROM {table}")


# noinspection LongLine
def create_process_mapping(processes: Dict[str, Process], func_name: str = None) -> None:
    """Creates or updates the processes mapping file.

    Args:
        processes: Dictionary of process names and the process.
        func_name: Function name of each process.

    See Also:
        - This is a special function, that uses doc strings to create a python dict.

    Handles:
        - speech_synthesis_api: Speech Synthesis
        - telegram_api: Telegram Bot
        - jarvis_api: Offline communicator, Robinhood portfolio report, Jarvis UI, Stock monitor, Surveillance, Telegram
        - background_tasks: Home automation, Alarms, Reminders, Meetings and Events sync, Wi-Fi connector, Cron jobs, Background tasks
        - plot_mic: Plot microphone usage in real time
    """
    impact_lib = {}
    for doc in create_process_mapping.__doc__.split('Handles:')[1].splitlines():
        if doc.strip():
            element = doc.strip().split(':')
            func = element[0].lstrip('- ')
            desc = element[1].strip().split(', ')
            if processes.get(func):
                impact_lib[func] = desc
            else:
                logger.warning("'%s' not found in list of processes initiated", func)
    if not func_name and sorted(impact_lib.keys()) != sorted(processes.keys()):
        warnings.warn(message=f"{list(impact_lib.keys())} does not match {list(processes.keys())}")
    if func_name:  # Assumes a processes mapping file exists already, since flag passed during process specific restart
        dump = process_map.get()
        dump[func_name] = {processes[func_name].pid: impact_lib[func_name]}
    else:
        dump = {k: {v.pid: impact_lib[k]} for k, v in processes.items()}
        dump["jarvis"] = {models.settings.pid: ["Main Process"]}
    logger.debug("Processes data: %s", dump)
    process_map.add(dump)


def start_processes(func_name: str = None) -> Union[Process, Dict[str, Process]]:
    """Initiates multiple background processes to achieve parallelization.

    Args:
        func_name: Name of the function that has to be started.

    Returns:
        Union[Process, Dict[str, Process]]:
        Returns a process object if a function name is passed, otherwise a mapping of function name and process objects.

    See Also:
        - speech_synthesis_api: Initiates docker container for speech synthesis.
        - telegram_api: Initiates polling Telegram API to execute offline commands (if no webhook config is available)
        - jarvis_api: Initiates uvicorn server to process API requests, stock monitor and robinhood report generation.
        - background_tasks: Initiates internal background tasks, cron jobs, alarms, reminders, events and meetings sync.
        - plot_mic: Initiates plotting realtime microphone usage using matplotlib.
    """
    process_dict = {
        jarvis_api.__name__: Process(target=jarvis_api),  # no process map removal
        offline.background_tasks.__name__: Process(target=offline.background_tasks),  # no process map removal
        speech_synthesis.speech_synthesis_api.__name__: Process(target=speech_synthesis.speech_synthesis_api),
        telegram.telegram_api.__name__: Process(target=telegram.telegram_api)
    }
    if models.env.plot_mic:
        statement = shutil.which(cmd="python") + " " + graph_mic.__file__
        process_dict[graph_mic.plot_mic.__name__] = Process(
            target=crontab.executor,
            kwargs={'statement': statement,
                    'log_file': datetime.now().strftime(os.path.join('logs', 'mic_plotter_%d-%m-%Y.log')),
                    'process_name': graph_mic.plot_mic.__name__}
        )
    # Used when a single process is requested to be triggered
    processes: Dict[str, Process] = {func_name: process_dict[func_name]} if func_name else process_dict
    for func, process in processes.items():
        process.name = func
        process.start()
        logger.info("Started function: {func} with PID: {pid}".format(func=func, pid=process.pid))
    Thread(target=create_process_mapping, kwargs=dict(processes=processes, func_name=func_name)).start()
    return processes[func_name] if func_name else processes


def stop_child_processes() -> None:
    """Stops sub processes (for meetings and events) triggered by child processes."""
    children: Dict[str, List[int]] = {}
    with db.connection:
        cursor = db.connection.cursor()
        for child in models.TABLES["children"]:
            # Use f-string or %s as condition cannot be parametrized
            data = cursor.execute(f"SELECT {child} FROM children").fetchall()
            children[child]: List[int] = util.matrix_to_flat_list([list(filter(None, d)) for d in data if any(d)])
    logger.info(children)  # Include empty lists so logs have more information but will get skipped when looping anyway
    for category, pids in children.items():
        for pid in pids:
            try:
                proc = psutil.Process(pid=pid)
            except psutil.NoSuchProcess:
                # Occurs commonly since child processes run only for a short time and `INSERT or REPLACE` leaves dupes
                logger.debug("Process [%s] PID not found %d", category, pid)
                continue
            logger.info("Stopping process [%s] with PID: %d", category, pid)
            support.stop_process(pid=proc.pid)


def stop_processes(func_name: str = None) -> None:
    """Stops all background processes initiated during startup and removes database source file."""
    stop_child_processes() if not func_name else None
    for func, process in shared.processes.items():
        if func_name and func_name != func:
            continue
        logger.info("Stopping process [%s] with PID: %d", func, process.pid)
        support.stop_process(pid=process.pid)
