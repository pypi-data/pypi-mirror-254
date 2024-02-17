from py_dreambooth.dataset import LocalDataset
from py_dreambooth.model import SdDreamboothModel
from py_dreambooth.trainer import LocalTrainer
from py_dreambooth.utils.image_helpers import display_images
from py_dreambooth.utils.prompt_helpers import make_prompt

class img_finetune:
    def __init__(self, data_dir="data", output_dir="models", subject_name="<YOUR-NAME>", class_name="person"):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.subject_name = subject_name
        self.class_name = class_name
        self.dataset = None
        self.model = None
        self.trainer = None
        self.predictor = None

    def prepare_data(self):
        self.dataset = LocalDataset(self.data_dir)
        self.dataset = self.dataset.preprocess_images(detect_face=True)

    def training(self):
        self.model = SdDreamboothModel(subject_name=self.subject_name, class_name=self.class_name)
        self.trainer = LocalTrainer(output_dir=self.output_dir)
        self.predictor = self.trainer.fit(self.model, self.dataset)

    def generate_image(self, prompt = None,prompt_height=768, prompt_width=512, num_images_per_prompt=2, fig_size=10):
        if prompt == None:
            prompt = next(make_prompt(self.subject_name, self.class_name))
        images = self.predictor.predict(prompt, height=prompt_height, width=prompt_width, num_images_per_prompt=num_images_per_prompt)
        display_images(images, fig_size=fig_size)