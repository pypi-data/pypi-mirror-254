import sys
import argparse
from llm_party.controller.session_controller import start_session_controller, start_session_with_first_message_controller

def main():
    parser = argparse.ArgumentParser(description='Start a chat session.')
    parser.add_argument('--mode', choices=['start', 'start_with_first_message'], required=True, help='Mode to run the script in.')
    parser.add_argument('--config_file_path', required=True, help='Path to the configuration file.')
    parser.add_argument('--first_message', help='The first message to send in the chat session.')
    parser.add_argument('--sender_name', help='The name of the sender of the first message.')
    parser.add_argument('--sender_role', help='The role of the sender of the first message.')
    parser.add_argument('--sender_type', help='The type of the sender of the first message.')
    parser.add_argument('--sender_attendee_params', help='Additional parameters for the sender of the first message.')
    parser.add_argument('--save_dir', help='Directory to save the chat session.')
    parser.add_argument('--save_file_name', help='File name to save the chat session.')
    try:
        args = parser.parse_args()
    except SystemExit as e:
        print(f"Error: {e}", file=sys.stderr)
        raise  # Re-raise the exception after printing the error message

    if args.mode == 'start':
        start_session_controller(args.config_file_path, args.save_dir, args.save_file_name)
    elif args.mode == 'start_with_first_message':
        start_session_with_first_message_controller(args.config_file_path, args.first_message, args.sender_name, args.sender_role, args.sender_type, args.sender_attendee_params, args.save_dir, args.save_file_name)

if __name__ == '__main__':
    main()