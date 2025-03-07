## Weaviate Python Dev Environment

This repository contains a development environment for Python projects, including a Docker-based Weaviate instance.

### Setup

First, copy this repository to your local machine:

```shell
git clone git@github.com:databyjp/weaviate-python-dev-env.git
```

Move into the directory:

```shell
cd weaviate-python-dev-env
```

Install VSCode if you don't have it already.
Then, open the project in VSCode:

```shell
code .
```

This will open VSCode.

You may be prompted "Folder contains a Dev Container configuration file. Reopen folder to develop in a container". Click "Reopen in Container".

If not:
- Install the "Dev Containers" extension in VSCode (by Microsoft), if you don't have it already.
- Open the command palette (Ctrl+Shift+P / Cmd+Shift+P) and type "Rebuild and Reopen in Container".

You should see a popup at the bottom right corner, indicating that the project is being reopened in a container.

When the container is ready, you should see a terminal in VSCode.
- It should include messages from a `pip install ...` command, indicating packages being installed.
- It should finish with a message like: `Done. Press any key to close the terminal.`
- Press enter, and you should be in a terminal window, with a prompt such as `/workspaces/app#`

Run the following command to check that everything is running:

```shell
python demo.py
```

You should see an output, like:

```shell
Weaviate is ready to use
Weaviate running with version: 1.29.0
```

Then, you are good to go!

### Connecting to Weaviate

Note that in this environment, the Weaviate instance has the hostname `weaviate`, not `localhost`. This is because the Weaviate instance is running in a Docker-based network.

So, in your Python code - connect to it like this:

```python
client = weaviate.connect_to_local(
    host="weaviate",
)
```
