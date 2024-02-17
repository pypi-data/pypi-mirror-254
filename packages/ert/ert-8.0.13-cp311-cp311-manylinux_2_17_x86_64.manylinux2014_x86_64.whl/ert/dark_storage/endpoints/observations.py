from typing import Any, List, Mapping
from uuid import UUID

from ert_storage import json_schema as js
from fastapi import APIRouter, Body, Depends

from ert.dark_storage.enkf import LibresFacade, get_res
from ert.shared.storage.extraction import create_observations

router = APIRouter(tags=["ensemble"])

DEFAULT_LIBRESFACADE = Depends(get_res)
DEFAULT_BODY = Body(...)


@router.post(
    "/experiments/{experiment_id}/observations", response_model=js.ObservationOut
)
def post_observation(
    *,
    res: LibresFacade = DEFAULT_LIBRESFACADE,
    obs_in: js.ObservationIn,
    experiment_id: UUID,
) -> js.ObservationOut:
    raise NotImplementedError


@router.get(
    "/experiments/{experiment_id}/observations", response_model=List[js.ObservationOut]
)
def get_observations(
    *, res: LibresFacade = DEFAULT_LIBRESFACADE, experiment_id: UUID
) -> List[js.ObservationOut]:
    return [
        js.ObservationOut(
            id=UUID(int=0),
            userData=[],
            errors=obs["errors"],
            values=obs["values"],
            x_axis=obs["x_axis"],
            name=obs["name"],
        )
        for obs in create_observations(res)
    ]


@router.get(
    "/ensembles/{ensemble_id}/observations", response_model=List[js.ObservationOut]
)
def get_observations_with_transformation(
    *, res: LibresFacade = DEFAULT_LIBRESFACADE, ensemble_id: UUID
) -> List[js.ObservationOut]:
    raise NotImplementedError


@router.put("/observations/{obs_id}/userdata")
async def replace_observation_userdata(
    *,
    res: LibresFacade = DEFAULT_LIBRESFACADE,
    obs_id: UUID,
    body: Any = DEFAULT_BODY,
) -> None:
    raise NotImplementedError


@router.patch("/observations/{obs_id}/userdata")
async def patch_observation_userdata(
    *,
    res: LibresFacade = DEFAULT_LIBRESFACADE,
    obs_id: UUID,
    body: Any = DEFAULT_BODY,
) -> None:
    raise NotImplementedError


@router.get("/observations/{obs_id}/userdata", response_model=Mapping[str, Any])
async def get_observation_userdata(
    *,
    res: LibresFacade = DEFAULT_LIBRESFACADE,
    obs_id: UUID,
) -> Mapping[str, Any]:
    raise NotImplementedError
