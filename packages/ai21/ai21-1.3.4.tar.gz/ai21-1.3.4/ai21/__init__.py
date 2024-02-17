import warnings

# Using stacklevel=2 to point to the caller of the deprecated function when making the actual call to ai21 package
warnings.warn("This version is being deprecated and will be removed in the future."
              " Please use version >= 2.0.0. "
              "For more information go to - https://github.com/AI21Labs/ai21-python", DeprecationWarning, stacklevel=2)

from ai21.constants import STUDIO_HOST, DEFAULT_API_VERSION, BedrockModelID
from ai21.modules.chat import Chat
from ai21.modules.completion import Completion
from ai21.modules.dataset import Dataset
from ai21.modules.tokenization import Tokenization
from ai21.modules.custom_model import CustomModel
from ai21.modules.experimental import Experimental
from ai21.modules.paraphrase import Paraphrase
from ai21.modules.summarize import Summarize
from ai21.modules.summarize_by_segment import SummarizeBySegment
from ai21.modules.segmentation import Segmentation
from ai21.modules.improvements import Improvements
from ai21.modules.question_answering import Answer
from ai21.modules.sagemaker import SageMaker
from ai21.modules.library import Library
from ai21.modules.gec import GEC
from ai21.modules.embed import Embed
from ai21.modules.destination import BedrockDestination, AI21Destination, SageMakerDestination
from ai21.version import __version__

api_key = None
organization = None
application = None
api_version = DEFAULT_API_VERSION
api_host = STUDIO_HOST
timeout_sec = None
num_retries = None
aws_region = None
log_level = 'warning'
