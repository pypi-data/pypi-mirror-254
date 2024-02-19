import argparse


class Cloud_Utils:
    def _parse_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument("--run_id", help="Id of the batch", type=int, required=True)
        parser.add_argument(
            "--policy_id", help="Id of the collection of files", type=int, required=True
        )
        return parser.parse_args()
