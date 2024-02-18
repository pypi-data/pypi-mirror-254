from typing import Any, Dict

from .common import (
    get_commander_and_metadata,
)
from .protobufs.bauplan_pb2 import (
    DeleteBranchRequest,
    GetBranchesRequest,
    GetBranchRequest,
    GetTableRequest,
)


def get_branches() -> Dict[str, Any]:
    client, metadata = get_commander_and_metadata()

    response = client.GetBranches(GetBranchesRequest(), metadata=metadata)
    return response.data.branches


def get_branch(branch_name: str) -> Dict[str, Any]:
    client, metadata = get_commander_and_metadata()

    response = client.GetBranch(GetBranchRequest(branch_name=branch_name), metadata=metadata)
    return response.data.entries


def delete_branch(branch_name: str) -> None:
    client, metadata = get_commander_and_metadata()

    client.DeleteBranch(DeleteBranchRequest(branch_name=branch_name), metadata=metadata)


def get_table(branch_name: str, table_name: str) -> Dict[str, Any]:
    client, metadata = get_commander_and_metadata()

    response = client.GetTable(
        GetTableRequest(branch_name=branch_name, table_name=table_name),
        metadata=metadata,
    )
    return response.data.entry.fields
