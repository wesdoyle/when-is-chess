# when-is-chess

This app outputs chess events for the current month at public Libraries in Madison.

## Description

This script scrapes the Madison Public Library calendar for chess events and prints them to the console.

Requests are cached using local file storage for 24 hours. The library website is pretty slow, so the first request takes up to 10 seconds.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/when-is-chess.git
    cd when-is-chess
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the script:**
    ```bash
    python when-is-chess.py
    ```

## Alias (Optional)

For quick lookup, you can add an alias to your `~/.zshrc` or `~/.bashrc` file:

```bash
alias chesscal="python /path/to/when-is-chess.py"
```
