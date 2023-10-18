from pydriller import Repository
from argparse import ArgumentParser
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime

@dataclass_json
@dataclass
class ModifiedFunction:
    name: str
    first_commit_date: datetime
    last_commit_date: datetime
    num_commits: int

def main():
    parser = ArgumentParser()
    parser.add_argument('--path', help='path to the repository', type=str, required=True)
    parser.add_argument('--topn', help='number of top modified functions to show', type=int, default=10)
    args = parser.parse_args()

    modified_functions = {}

    commits = Repository(args.path, only_in_branch='main',only_modifications_with_file_types=['.py','.js','.java','.ts']).traverse_commits()
    start_date = datetime.today()
    end_date = datetime(1000, 1, 1)

    for commit in commits:
        for modified_file in commit.modified_files:
            changed_methods = modified_file.changed_methods
            for changed_method in changed_methods:
                method_path = f"{modified_file.new_path}#{changed_method.name}"

                if commit.committer_date < start_date:
                    start_date = commit.committer_date
                
                if commit.committer_date > end_date:
                    end_date = commit.committer_date

                if method_path not in modified_functions.keys():
                    modified_functions[method_path] = ModifiedFunction(name=changed_method.name, first_commit_date=start_date, last_commit_date=end_date, num_commits=1)
                else:
                    modified_functions[method_path].num_commits += 1
                    modified_functions[method_path].last_commit_date = end_date
                    modified_functions[method_path].first_commit_date = start_date     

    sorted_modified_functions = sorted(modified_functions.items(), key=lambda x: x[1], reverse=True)

    print("## Top modified functions in this repo")

    print(f"The repo has {len(list(commits))} commits and a total of {len(modified_functions)} modified functions")
    print(f"Top {args.topn} modified functions:\n")

    print(f"| Function | # commits | Date Range |") 
    print(f"| --- | --: | --: |")
    for function in sorted_modified_functions[:10]:
        print(f"| {function[0]} | {function[1].num_commits} | {function[1].first_commit_date.strftime('%d/%m/%Y')} - {function[1].last_commit_date.strftime('%d/%m/%Y')} |")

if __name__ == "__main__":
    main()
