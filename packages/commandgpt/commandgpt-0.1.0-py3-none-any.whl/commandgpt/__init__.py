#!/usr/bin/env python3
import os
import logging
import argparse
import configparser
from pathlib import Path
from openai import OpenAI

__version__ = "0.1.0"

# Constants
DEFAULT_MODEL = "gpt-3.5-turbo"
CONFIG_PATH = Path.home() / ".openai_config"

# Setting the basic configuration for logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class OpenAIChat:
    """
    A class to interact with the OpenAI API for chat functionalities.

    Instance Attributes:
        api_key (str): The API key to access OpenAI services.
        model (str): The model to use for the chat interactions.
        default_system_msg (str): The default system message to set the context for GPT.
        default_user_msg (str): The default prefix for user messages.

    Methods:
        chat(system_msg: str, user_prefix: str, query: str) -> str:
            Sends a message to the OpenAI API and retrieves the response.

        __initialize_config(reconfigure: bool = False) -> None:
            Private method to initialize or read the API configuration.
    """

    def __init__(self, reconfigure=False):
        """
        Initializes the OpenAIChat instance with the OpenAI API key and the desired model.

        """
        self.api_key = None
        self.model = None
        self.default_system_msg = None
        self.default_user_msg = None
        self.__initialize_config(reconfigure=reconfigure)
        self.client = OpenAI(api_key=self.api_key)

    def chat(self, system_msg, user_prefix, query):
        """
        Sends a message to the OpenAI API and retrieves the response.

        Parameters:
            system_msg (str): System message to set the context for GPT.
            user_prefix (str): Prefix for the user message.
            query (str): The user's query.

        Returns:
            str: The response from the OpenAI API.
        """
        if system_msg is None:
            system_msg = self.default_system_msg
        if user_prefix is None:
            user_prefix = self.default_user_msg

        if system_msg is None or user_prefix is None:
            raise ValueError("System message and user prefix must be non-null strings")

        user_msg = f"{user_prefix} {query}"
        try:
            logging.debug(
                f"Sending request with system_msg: {system_msg}, user_msg: {user_msg}"
            )
            response = self.client.chat.completions.create(model=self.model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ])
            return response.choices[0].message.content

        except openai.AuthenticationError:  # Add this exception
            logging.error("AuthenticationError encountered", exc_info=True)
        except openai.RateLimitError:
            logging.error("RateLimitError encountered", exc_info=True)
        except openai.OpenAIError as e:
            logging.error("OpenAIError encountered", exc_info=True)
        except Exception as e:
            logging.error("Unexpected error occurred", exc_info=True)

    def __initialize_config(self, reconfigure=False):
        """
        Private method to initialize or read the API configuration.

        Parameters:
            reconfigure (bool): If True, reconfigures API settings even if a configuration already exists.
        """
        if CONFIG_PATH.exists() and not reconfigure:
            # Check file permissions
            if oct(os.stat(CONFIG_PATH).st_mode)[-3:] != '600':
                logging.warning("Config file permissions are not secure. Attempting to fix.")
                try:
                    os.chmod(CONFIG_PATH, 0o600)
                    logging.info("Config file permissions fixed to 0o600.")
                except Exception as e:
                    logging.error(f"Failed to fix config file permissions: {e}")
                    raise

            config = configparser.ConfigParser()
            config.read(CONFIG_PATH)
            self.api_key = config["DEFAULT"].get("OPENAI_API_KEY", "").strip()
            if not self.api_key:
                raise ValueError("The API key in the config file is empty.")
            self.model = config["DEFAULT"].get("OPENAI_MODEL", DEFAULT_MODEL).strip()
            self.default_system_msg = config["DEFAULT"].get("SYSTEM_MSG", "")
            self.default_user_msg = config["DEFAULT"].get("USER_MSG", "")
            logging.debug(
                (
                    f"Loaded config: API_KEY={self.api_key}, MODEL={self.model},"
                    f"SYSTEM={self.default_system_msg}, USER={self.default_user_msg}"
                )
            )
        else:
            if CONFIG_PATH.exists():
                logging.info("You are about to modify an existing configuration.")
            self.api_key = input("Enter your OpenAI API key: ").strip()
            while not self.api_key:
                print("Please provide a valid API key.")
                self.api_key = input("Enter your OpenAI API key: ").strip()

            print("Choose a model:")
            print("1: gpt-3.5-turbo (default)")
            print("2: gpt-4")
            choice = input("Choice: ").strip()

            if choice not in ["1", "2", ""]:
                print("Invalid choice. Using the default model.")
                choice = "1"

            self.model = DEFAULT_MODEL if choice == "1" or not choice else "gpt-4"

            # Prompting for default system and user messages
            self.default_system_msg = input(
                "Enter the default system message: "
            ).strip()
            self.default_user_msg = input("Enter the default user message: ").strip()

            # Save the choices to the config file
            config = configparser.ConfigParser()
            config["DEFAULT"] = {
                "OPENAI_API_KEY": self.api_key,
                "OPENAI_MODEL": self.model,
                "SYSTEM_MSG": self.default_system_msg,
                "USER_MSG": self.default_user_msg,
            }
            with CONFIG_PATH.open("w") as config_file:
                config.write(config_file)
            os.chmod(CONFIG_PATH, 0o600)
            logging.debug(f"Configurations saved to {CONFIG_PATH}")


def main():
    """
    The main function to interact with OpenAI GPT from the command line.
    Parses command-line arguments, interacts with the OpenAI API, and prints the response.
    """
    parser = argparse.ArgumentParser(description="Interact with OpenAI ChatGPT.")

    parser.add_argument(
        "query", type=str, nargs="?", default=None, help="your question or query"
    )
    parser.add_argument(
        "-s",
        "--system",
        type=str,
        help="system message for AI",
    )

    parser.add_argument(
        "-u",
        "--user",
        type=str,
        help="prefix for user message",
    )
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode")
    parser.add_argument(
        "-c", "--config", action="store_true", help="reconfigure settings"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="show the version number and exit",
    )
    args = parser.parse_args()
    if args.query is None and not (args.system or args.user or args.config):
        parser.print_help()
        return

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.ERROR)

    try:
        chatbot = OpenAIChat(reconfigure=args.config)
        response = chatbot.chat(args.system, args.user, args.query)
        if response:
            print(response)
    except ValueError as e:
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
