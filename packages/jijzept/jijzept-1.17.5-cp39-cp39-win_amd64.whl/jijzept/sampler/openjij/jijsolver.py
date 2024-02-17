from __future__ import annotations

import typing as typ

from dataclasses import dataclass

import jijmodeling as jm

from jijzept.entity.schema import SolverType
from jijzept.response import JijModelingResponse
from jijzept.sampler.base_sampler import (
    JijZeptBaseSampler,
    ParameterSearchParameters,
    check_kwargs_against_dataclass,
    merge_params_and_kwargs,
    sample_instance,
    sample_model,
)
from jijzept.type_annotation import FixedVariables, InstanceData

T = typ.TypeVar("T")


@dataclass
class JijSolverParameters:
    """Manage Parameters for using JijSolver's WeightedLS.

    Attributes:
        numiters (int): The number of iterations (each iteration consists of SFSA, SFLS, MFLS, and update of the weights)
        eachsamsecs (float): How long does the solver take for each SA (LS) part (in units of millisecond)
    """

    numiters: int = 4
    eachsamsecs: float = 2000


class JijSolver(JijZeptBaseSampler):
    jijmodeling_solver_type = SolverType(queue_name="openjijsolver", solver="JijSolver")

    def sample_model(
        self,
        model: jm.Problem,
        feed_dict: InstanceData,
        fixed_variables: FixedVariables = {},
        parameters: JijSolverParameters = JijSolverParameters(),
        max_wait_time: int | float | None = None,
        sync: bool = True,
        queue_name: str | None = None,
        **kwargs,
    ) -> JijModelingResponse:
        check_kwargs_against_dataclass(kwargs, JijSolverParameters)
        param_dict = merge_params_and_kwargs(parameters, kwargs, JijSolverParameters)

        para_search_params = ParameterSearchParameters()

        if queue_name is None:
            queue_name = self.jijmodeling_solver_type.queue_name

        sample_set = sample_model(
            self.client,
            self.jijmodeling_solver_type.solver,
            queue_name=queue_name,
            problem=model,
            instance_data=feed_dict,
            fixed_variables=fixed_variables,
            parameter_search_parameters=para_search_params,
            max_wait_time=max_wait_time,
            sync=sync,
            **param_dict,
        )
        return sample_set

    def sample_instance(
        self,
        instance_id: str,
        fixed_variables: FixedVariables = {},
        parameters: JijSolverParameters = JijSolverParameters(),
        max_wait_time: int | float | None = None,
        sync: bool = True,
        queue_name: str | None = None,
        system_time: jm.SystemTime = jm.SystemTime(),
        **kwargs,
    ) -> JijModelingResponse:
        check_kwargs_against_dataclass(kwargs, JijSolverParameters)
        param_dict = merge_params_and_kwargs(parameters, kwargs, JijSolverParameters)

        para_search_params = ParameterSearchParameters()

        if queue_name is None:
            queue_name = self.jijmodeling_solver_type.queue_name

        sample_set = sample_instance(
            client=self.client,
            solver=self.jijmodeling_solver_type.solver,
            queue_name=queue_name,
            instance_id=instance_id,
            fixed_variables=fixed_variables,
            parameter_search_parameters=para_search_params,
            max_wait_time=max_wait_time,
            sync=sync,
            system_time=system_time,
            **param_dict,
        )

        return sample_set
