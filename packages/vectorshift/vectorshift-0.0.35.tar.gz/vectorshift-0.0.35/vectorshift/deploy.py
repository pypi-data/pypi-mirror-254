# functionality to deploy and run pipelines 
import vectorshift
from vectorshift.pipeline import Pipeline

class Config:
    # For now, the config is just a wrapper for the API key
    def __init__(self, public_key = None, private_key = None):
        self.public_key = public_key or vectorshift.public_key
        self.private_key = private_key or vectorshift.private_key

    # Save the pipeline as a new pipeline to the VS platform.
    def save_new_pipeline(self, pipeline: Pipeline) -> dict:
        # already implemented in the Pipeline class
        # save method will itself raise an exception if 200 isn't returned
        response = pipeline.save(
            public_key=self.public_key,
            private_key=self.private_key,
            update_existing=False
        )
        return response

    # Update the pipeline, assuming it already exists in the VS platform.
    # Raises if the pipeline ID doesn't exist, or isn't in the VS platform.
    def update_pipeline(self, pipeline: Pipeline) -> dict:
        response = pipeline.save(
            public_key=self.public_key,
            private_key=self.private_key,
            update_existing=True
        )
        
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()
