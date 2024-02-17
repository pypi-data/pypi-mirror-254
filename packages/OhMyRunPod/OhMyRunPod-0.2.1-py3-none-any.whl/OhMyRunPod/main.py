import argparse
from OhMyRunPod.modules.ssh_setup.ssh_setup import run_ssh_setup_script
from OhMyRunPod.modules.pod_info import print_pod_info

def main():
    parser = argparse.ArgumentParser(description="OhMyRunPod Command Line Tool")
    parser.add_argument('--setup-ssh', action='store_true', help='Run the SSH setup script')
    parser.add_argument('--info', action='store_true', help='Display information about the Pod')

    args = parser.parse_args()

    if args.setup_ssh:
        run_ssh_setup_script()

    if args.info:
        print_pod_info()

if __name__ == "__main__":
    main()
