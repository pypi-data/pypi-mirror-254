from typing import Any, Optional

import ray

from xflow.deploy.types import IOSignature
from xflow.model.structures import ModelTypes
from xflow.model.metric import Metric
from xflow._utils.decorators import executor_method
from xflow._private._constants import Actors


@executor_method
def export_model(model_name: str, model_type: str, model_object: Any,
                 model_input: list[IOSignature], model_output: list[IOSignature], metric: Optional[list[Metric]] = None,
                 description: str = ''):
    if model_type not in list(ModelTypes().__dict__.values()):
        raise ValueError(f"unsupported model type {model_type}. use ModelTypes class in xflow.model")
    if not isinstance(model_input, list):
        raise ValueError(f"unsupported model signature {model_input}. use ModelSignature class in xflow.model")
    else:
        for _ in model_input:
            if not isinstance(_, IOSignature):
                raise ValueError(f"unsupported model signature {model_input}. use ModelSignature class in xflow.model")
    if not isinstance(model_output, list):
        raise ValueError(f"unsupported model signature {model_output}. use ModelSignature class in xflow.model")
    else:
        for _ in model_output:
            if not isinstance(_, IOSignature):
                raise ValueError(f"unsupported model signature {model_input}. use ModelSignature class in xflow.model")
    try:
        actor_id = ray.get_runtime_context().get_actor_id()
        manager_actor = ray.get_actor(Actors.MANAGER)
        owner_actor = ray.get(manager_actor.get_pool_actor_owner.remote(actor_id))
        owner_actor = ray.get_actor(owner_actor)
        project, pipeline, rev, trial, reg_id = ray.get(owner_actor.get_pipeline_info.remote())
        xflow_worker_actor = ray.get_actor(Actors.XFLOW_WORKER)
    except Exception as exc:
        raise RuntimeError(f"can't get pipeline runtime context. {exc.__str__()}")
    try:
        ref = ray.put(model_object)
        ray.get(xflow_worker_actor.export_model.remote(project=project, pipeline=pipeline, revision=rev, trial=trial,
                                                       model_name=model_name,  model_type=model_type, metric=metric,
                                                       model_input=model_input, model_output=model_output,
                                                       model_object=ref, description=description, reg_id=reg_id))
        del ref
    except Exception as exc:
        raise RuntimeError(f"failed to export model. {exc.__str__()}")
    print(f"export model: {model_name} success")
