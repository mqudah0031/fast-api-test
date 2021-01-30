from worker_client import celery


def send_confirmation_email(user) -> None:
    """
    sends a confirmation email to the user email
    :param user: user object
    :return:
    """
    celery.send_task("worker.email.email", (user.email, "Confirmation", "you've created an account at ...."))
