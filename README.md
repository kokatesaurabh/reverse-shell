# Remote Access Trojan (RAT) - Reverse Shell

Welcome to the **Remote Access Trojan (RAT)** project! This Python-based tool demonstrates basic remote command execution capabilities. It consists of two main components:

- **Server (`server.py`)**: Listens for client connections and sends commands.
- **Client (`rat.py`)**: Connects to the server, executes commands, and sends back results.

## Features

- **Real-time Command Execution**: Execute commands on the client machine remotely.
- **Instant Feedback**: Receive command output from the client in real-time.
- **Simple Setup**: Easy-to-use scripts for quick deployment.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kokatesaurabh/reverse-shell.git
    cd reverse-shell
    ```

2. Install any required dependencies (currently none):
    ```bash
    pip install -r requirements.txt
    ```

### Usage

#### Server Setup

1. Run the server script:
    ```bash
    python server.py
    ```

2. The server will start listening for incoming connections on the specified IP and port.

#### Client Setup

1. Edit `rat.py` to set the `SERVER_IP` variable to the server’s IP address.

2. Run the client script:
    ```bash
    python rat.py
    ```

3. The client will connect to the server and be ready to execute commands.

### Commands

- **On Server**:
  - Type commands and press Enter to send them to the connected client.
  - Use `quit`, `exit`, `q`, or `x` to disconnect the client and stop the server.

- **On Client**:
  - Executes commands received from the server and sends back the output.

## Important Notes

- **Ethical Use**: This project is for educational purposes only. Unauthorized use on other systems is illegal and unethical.
- **Security**: Use this tool only in a controlled, authorized environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [Saurabh Kokate](https://www.linkedin.com/in/saurabh-kokate-b839b921a).

---

Happy learning and exploring!
