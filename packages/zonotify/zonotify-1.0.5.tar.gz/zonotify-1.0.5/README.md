# Zonotify

Zonotify is a versatile Python package designed to provide convenient notification services for developers and users working on extensive tasks. Born out of the need for staying updated on the status of long-running tasks without the hassle of constantly checking the code, Zonotify simplifies the process by sending notifications directly through Discord or email. Whether you're running a complex data processing task, a lengthy machine learning model training, or any other time-consuming operation, Zonotify keeps you informed about the task's completion or progress updates, seamlessly integrating with just a few lines of code.

## Installation

Install Zonotify easily using pip:

```bash
pip install zonotify
```

## Usage
To use Zonotify, first import the package and set up the notifier for either Discord or email notifications or both.

```python
from zonotify import Zonotify

# Initialize with your Discord webhook URL and gmail credentials
notifier = Zonotify(discord_webhook_url='your_discord_webhook_url', gmail_credentials={
    'email': 'your_email@example.com',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'username': 'your_username',
    'password': 'your_password'
})
```


## Send a notification to Discord
```python
notifier.notify_discord('Task Completed', 'Your long-running task has finished.')
```
## Send a notification via Email
```python
notifier.notify_email('recipient@example.com', 'Task Status', 'Your task')
```

## Contributing
We welcome contributions from the community! If you have suggestions, improvements, or want to report an issue, please visit our GitHub repository. Your input is valuable to us, and we look forward to seeing your ideas and contributions!

## Conclusion
Zonotify aims to make the life of developers and users easier by automating the notification process for various tasks. It's a simple yet powerful tool that can be integrated into numerous workflows and systems. We hope Zonotify enhances your productivity and helps you stay updated on your tasks with minimal disruption. Happy coding!