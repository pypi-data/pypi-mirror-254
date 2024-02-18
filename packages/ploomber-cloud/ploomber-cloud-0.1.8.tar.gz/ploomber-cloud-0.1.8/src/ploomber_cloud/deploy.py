import click
import time

from ploomber_core.exceptions import modify_exceptions

from ploomber_cloud import api, zip_
from ploomber_cloud.config import PloomberCloudConfig
from ploomber_cloud.github import display_github_workflow_info_message

STATUS_COLOR = {
    "pending": "white",
    "active": "yellow",
    "finished": "green",
    "success": "green",
    "failed": "red",
    "inactive": "red",
    "stopped": "magenta",
}

FAILED_STATUSES = (
    "docker-failed",
    "provisioning-failed",
    "infrastructure-failed",
    "failed",
)

INTERVAL_SECS = 15.0
TIMEOUT_MINS = 15.0


def _unpack_job_status(job):
    """
    Format and output a job status message.
    Return job status (and URL if success).

    Parameters
    ----------
    job: JSON
        Contains job status information to output and process.

    Returns
    ----------
    job_status: str
        Status of job. Possible values: "success", "running", or "failed".

    app_url: str
        URL to view dashboard. Only returned if job_status == "success".
    """
    tasks = job["summary"]
    status_msg = []

    for name, status in tasks:
        status_msg.append(f"{name}: {click.style(status, fg=STATUS_COLOR[status])} | ")

    click.echo("".join(status_msg))

    # grab job status as reported by backend api
    status = job["status"]

    # job is running and reporting healthy
    if status == "running":
        return "success", job["resources"]["webservice"]

    # job has failed or stopped
    if status in FAILED_STATUSES:
        return "failed", None

    # job is still pending, continue watching
    return "pending", None


def _watch(client, project_id, job_id):
    start_time = time.time()
    interval = INTERVAL_SECS
    timeout = 60.0 * TIMEOUT_MINS

    # poll every 'interval' secs until 'timeout' mins
    while True:
        status_page = api.PloomberCloudEndpoints().status_page(project_id, job_id)

        curr_time = time.time()
        time_diff = curr_time - start_time

        if time_diff >= timeout:
            click.secho("Timeout reached.", fg="yellow")
            click.echo(f"For more details, go to: {status_page}")
            return

        curr_time_formatted = time.strftime("%H:%M:%S", time.localtime(curr_time))
        click.echo(f"[{curr_time_formatted}]:")

        # get job status from API and send it to be formatted/output
        job = client.get_job_by_id(job_id)
        job_status, app_url = _unpack_job_status(job)

        # deploy has either succeeded or failed
        if job_status != "pending":
            click.secho(f"Deployment {job_status}.", fg=STATUS_COLOR[job_status])
            click.echo(f"View project dashboard: {status_page}")
            if job_status == "success":
                click.echo(f"View your deployed app: {app_url}")
            break

        time.sleep(interval - (time_diff % interval))


@modify_exceptions
def deploy(watch):
    """Deploy a project to Ploomber Cloud, requires a project to be initialized"""
    client = api.PloomberCloudClient()
    config = PloomberCloudConfig()
    config.load()

    with zip_.zip_app(verbose=True) as (path_to_zip, env_variables):
        click.echo(f"Deploying project with id: {config.data['id']}...")
        output = client.deploy(
            path_to_zip=path_to_zip,
            project_type=config.data["type"],
            project_id=config.data["id"],
            env_variables=env_variables,
        )
        if watch:
            _watch(client, output["project_id"], output["id"])

    display_github_workflow_info_message()
