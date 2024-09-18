import logging

from core.model_runtime.entities.model_entities import ModelType
from core.model_runtime.errors.validate import CredentialsValidateFailedError
from core.model_runtime.model_providers.__base.model_provider import ModelProvider

logger = logging.getLogger(__name__)


class SeaMoneyProvider(ModelProvider):

    def validate_provider_credentials(self, credentials: dict) -> None:
        """
        Validate provider credentials
        if validate failed, raise exception

        :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
        """
        try:
            model_instance = self.get_model_instance(ModelType.LLM)

            # TODO: placeholder to pass credential check
            model_nm = "/home/work/.cache/huggingface/hub/models--OpenGVLab--InternVL2-40B-AWQ/snapshots/746114fc984c145a5730c2b93d7859edef888880"
            credentials["mode"] = "chat"

            model_instance.validate_credentials(
                model=model_nm,
                credentials=credentials
            )
        except CredentialsValidateFailedError as ex:
            raise ex
        except Exception as ex:
            logger.exception(f'{self.get_provider_schema().provider} credentials validate failed')
            raise ex
