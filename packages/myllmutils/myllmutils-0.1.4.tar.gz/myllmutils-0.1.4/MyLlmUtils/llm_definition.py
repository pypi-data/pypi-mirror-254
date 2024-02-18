import os
import configparser
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings, ChatOpenAI, OpenAIEmbeddings
from MyLlmUtils.commons import ProviderType


class LlmDefinition(object):
    """
    A class that represents an LLM definition.

    Args:
      provider: The name of the LLM provider.
    """

    def __init__(self, provider: ProviderType, config_file_path: str):
        self.provider = provider
        self.config_file_path = config_file_path
        self.cf = configparser.ConfigParser()
        self.cf.read(self.config_file_path)

    def __repr__(self):
        return "LmDefinition(provider={})".format(self.provider)

    def get_llm(self, **kwargs):
        if self.provider == ProviderType.AZURE:
            return self.__azure_llm(**kwargs)
        if self.provider == ProviderType.OPENAI:
            return self.__openai_llm(**kwargs)

    def get_embeddings(self):
        if self.provider == ProviderType.AZURE:
            return AzureOpenAIEmbeddings(deployment=self.cf[self.provider.value]["EMBEDDINGS_MODEL"])
        if self.provider == ProviderType.OPENAI:
            return OpenAIEmbeddings()

    def __azure_llm(self, **kwargs):
        self.__reset_env()

        os.environ["OPENAI_API_KEY"] = self.cf[self.provider.value]["API_KEY"]
        os.environ["OPENAI_API_TYPE"] = "azure"
        os.environ["OPENAI_API_VERSION"] = self.cf[self.provider.value]["API_VERSION"]
        os.environ["AZURE_OPENAI_ENDPOINT"] = self.cf[self.provider.value]["API_BASE"]
        os.environ["COMPLETIONS_MODEL"] = self.cf[self.provider.value]["COMPLETIONS_MODEL"]

        kwargs['deployment_name'] = os.environ["COMPLETIONS_MODEL"]
        return AzureChatOpenAI(**kwargs)

    def __openai_llm(self, **kwargs):
        self.__reset_env()

        os.environ["OPENAI_API_KEY"] = self.cf[self.provider.value]["API_KEY"]
        kwargs['model_name'] = self.cf[self.provider.value]["COMPLETIONS_MODEL"]
        return ChatOpenAI(**kwargs)

    @staticmethod
    def __reset_env():
        key_list = [k for k in dict(os.environ).keys() if 'OPENAI' in k]
        for key in key_list:
            os.environ.pop(key)


if __name__ == '__main__':
    from MyLlmUtils.commons import ProviderType
    from langchain.schema import HumanMessage
    from langchain_core.messages.base import BaseMessage
    llm_def = LlmDefinition(provider=ProviderType.AZURE, config_file_path="llm-config-gpt4.ini")
    llm = llm_def.get_llm()
    embeddings = llm_def.get_embeddings()
    message = HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    )
    answer:BaseMessage = llm.invoke([message])
    print(answer)

    text = "This is a test query."
    query_result = embeddings.embed_query(text)
    print(query_result)
