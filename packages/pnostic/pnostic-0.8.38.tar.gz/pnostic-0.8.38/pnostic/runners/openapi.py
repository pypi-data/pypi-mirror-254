from typing import List
import mystring
from pnostic.structure import RepoResultObject, Runner

class app(Runner):
	def __init__(self, openapi_key="", openapi_model="", prefix_for_prompt="",
			frequency_penalty=None, #: Optional[float] | NotGiven = NOT_GIVEN,
			function_call=None, #: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
			functions=None, #: List[completion_create_params.Function] | NotGiven = NOT_GIVEN,
			logit_bias=None, #: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
			logprobs=None, #: Optional[bool] | NotGiven = NOT_GIVEN,
			max_tokens=None, #: Optional[int] | NotGiven = NOT_GIVEN,
			n=None, #: Optional[int] | NotGiven = NOT_GIVEN,
			presence_penalty=None, #: Optional[float] | NotGiven = NOT_GIVEN,
			response_format=None, #: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
			seed=None, #: Optional[int] | NotGiven = NOT_GIVEN,
			stop=None, #: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
			temperature=None, #: Optional[float] | NotGiven = NOT_GIVEN,
			tool_choice=None, #: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
			tools=None, #: List[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
			top_logprobs=None, #: Optional[int] | NotGiven = NOT_GIVEN,
			top_p=None, #: Optional[float] | NotGiven = NOT_GIVEN,
			fix_response=lambda string:string,
	):
		super().__init__()
		self.openapi_key = openapi_key
		self.openapi_model = openapi_model
		self.prefix_for_prompt = prefix_for_prompt

		#Specific Chatgpt OpenAI Parameters
		self.frequency_penalty = frequency_penalty
		self.function_call = function_call
		self.functions = functions
		self.logit_bias = logit_bias
		self.logprobs = logprobs
		self.max_tokens = max_tokens
		self.n = n
		self.presence_penalty = presence_penalty
		self.response_format = response_format
		self.seed = seed
		self.stop = stop
		self.temperature = temperature
		self.tool_choice = tool_choice
		self.tools = tools
		self.top_logprobs = top_logprobs
		self.top_p = top_p
		self.fix_response = fix_response

		self.imports += [
			"openai==1.10.0", #https://github.com/openai/openai-python
			"tqdm==4.66.1",
			"backoff==2.2.1"
		]
		self.imports += self.browser.imports
		self.client = None

	def initialize(self) -> bool:
		print("Initializing")
		from openai import OpenAI
		self.client = OpenAI(
			api_key=self.openapi_key,
		)
		return True

	@staticmethod
	def __api_request_STALLED(response):
		for string in [
			"I couldn't complete your request.",
			"Rephrase your prompt",
			"outside of my capabilities",
			"I'm unable to help",
			"I can't help you with that",
			"I'm unable to",
		]:
			if string in response:
				return True

		return False

	def __api_wrapped_request(self, **kwargs):
		import backoff
		import openai

		current_client = self.client

		#Lazily Taken from https://github.com/litl/backoff
		def backoff_hdlr(details):
			print ("Backing off {wait:0.1f} seconds after {tries} tries "
				"calling function {target} with args {args} and kwargs "
				"{kwargs}".format(**details))

		#Lazily Taken from https://platform.openai.com/docs/guides/rate-limits/error-mitigation?context=tier-free
		@backoff.on_exception(backoff.expo, openai.RateLimitError,on_backoff=backoff_hdlr)
		def completions_with_backoff(**kwargs):
			return current_client.chat.completions.create.completions.create(**kwargs)
	
		
		startDateTime = mystring.current_date()
		resp =  completions_with_backoff(**kwargs)
		endDateTime = mystring.current_date()

		resp.startDateTime = startDateTime
		resp.endDateTime = endDateTime

		return resp

	def prep_messages(self, source_code):
		messages = []
		if self.prefix_for_prompt:
			messages += [{
				"role": "system",
				"content": self.prefix_for_prompt,
			}]

		messages += [{
			"role":"user",
			"content":"SOURCE="+self.fix_response(mystring.string.of(source_code).noNewLine(";"))
		}]

		return messages

	def __api_request(self,user_content):
		import time
		from tqdm import tqdm
		from openai import OpenAI
		from openai._types import NotGiven

		#Setting the extra parameters for OpenAI to NotGiven if None
		self.frequency_penalty = self.frequency_penalty or NotGiven()
		self.function_call = self.function_call or NotGiven()
		self.functions = self.functions or NotGiven()
		self.logit_bias = self.logit_bias or NotGiven()
		self.logprobs = self.logprobs or NotGiven()
		self.max_tokens = self.max_tokens or NotGiven()
		self.n = self.n or NotGiven()
		self.presence_penalty = self.presence_penalty or NotGiven()
		self.response_format = self.response_format or NotGiven()
		self.seed = self.seed or NotGiven()
		self.stop = self.stop or NotGiven()
		self.temperature = self.temperature or NotGiven()
		self.tool_choice = self.tool_choice or NotGiven()
		self.tools = self.tools or NotGiven()
		self.top_logprobs = self.top_logprobs or NotGiven()
		self.top_p = self.top_p or NotGiven()

		messages = []
		if self.prefix_for_prompt:
			messages += [{
				"role": "system",
				"content": self.prefix_for_prompt,
			}]

		messages += [{
			"role":"user",
			"content":user_content
		}]

		startDateTime = None
		endDateTime = None
		chat_completion = None
		full_response = None

		while chat_completion is None:
			try:
				#https://github.com/openai/openai-python/blob/0c1e58d511bd60c4dd47ea8a8c0820dc2d013d1d/src/openai/resources/chat/completions.py#L42
				chat_completion = self.__api_wrapped_request(
					messages=messages,
					model=self.openapi_model,
					#Extra Parameters for OpenAI
					frequency_penalty = self.frequency_penalty,
					function_call = self.function_call,
					functions = self.functions,
					logit_bias = self.logit_bias,
					logprobs = self.logprobs,
					max_tokens = self.max_tokens,
					n = self.n,
					presence_penalty = self.presence_penalty,
					response_format = self.response_format,
					seed = self.seed,
					stop = self.stop,
					temperature = self.temperature,
					tool_choice = self.tool_choice,
					tools = self.tools,
					top_logprobs = self.top_logprobs,
					top_p = self.top_p
				)
				if self.__api_request_STALLED(chat_completion):
					chat_completion = None
				else:
					#https://github.com/openai/openai-python/blob/0c1e58d511bd60c4dd47ea8a8c0820dc2d013d1d/examples/demo.py#L19
					full_response = str(chat_completion)
					startDateTime = chat_completion.startDateTime
					endDateTime = chat_completion.endDateTime
					chat_completion = chat_completion.choices[0].messages.content
			except openai.APIConnectionError as e:
				print("The server could not be reached")
				print(e.__cause__)  # an underlying Exception, likely raised within httpx.
				break
			except openai.RateLimitError as e:
				print("A 429 status code was received; we should back off a bit.")
				for _ in tqdm(range(60*5)):
					time.sleep(1)
			except openai.APIStatusError as e:
				print("Another non-200-range status code was received")
				print(e.status_code)
				print(e.response)
				break

		return {
			"CHAT":chat_completion,
			"FULL":full_response,
			"START":startDateTime,
			"STOP":endDateTime,
		}

	def scan(self, filePath: str) -> List[RepoResultObject]:
		import json

		with open(file, "r") as reader:
			content = '\n'.join(reader.readlines())

		chat_and_full = self.__api_request("")
		chat,raw,startDateTime,endDateTime = chat_and_full["CHAT"],chat_and_full["FULL"],chat_and_full["START"],chat_and_full["STOP"]

		return [RepoResultObject(
			projecttype="",
			projectname=self.name(),
			projecturl="",
			qual_name="",
			tool_name=self.name(),
			Program_Lines=-1,
			Total_Lines=content.count("\n"),
			Number_of_Imports=-1,
			MCC=-1,
			IsVuln=None,
			ruleID=None,
			cryptolationID=-1,
			CWEId=None,
			Message=mystring.obj_to_string(raw, prefix="json:").tobase64(prefix="b64:"),
			Exception=None,
			llmPrompt=mystring.string.of(
				self.prep_messages(content)
			).tobase64(prefix="b64:"),
			llmResponse=mystring.string.of(chat).tobase64(prefix="b64:"),
			extraToolInfo="",
			fileContent=mystring.string.of(content).tobase64(prefix="b64:"),
			Line=-1,
			correctedCode=None,
			severity="",
			confidence="",
			context="",
			TP=0,
			FP=0,
			TN=0,
			FN=0,
			dateTimeFormat="ISO",
			startDateTime=str(mystring.date_to_iso(startDateTime)),
			endDateTime=str(mystring.date_to_iso(endDateTime)),
		)]

	def name(self) -> mystring.string:
		return mystring.string.of("OpenAPI_{0}".format(self.openapi_model))

	def clean(self) -> bool:
		print("Cleaning")
		self.client = None
		return True

	def arg_init_string(self)->str:
		return ""