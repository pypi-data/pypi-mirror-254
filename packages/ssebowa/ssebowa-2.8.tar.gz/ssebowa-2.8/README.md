# Ssebowa
Ssebowa is an open source Python library that provides  generative AI models, including:

For more detailed usage information, please refer to: [Ssebowa's technical documentation](https://ssebowa.ai) 



## Usage

Before running the script, ensure that the required libraries are installed. You can do this by executing the following commands:

```bash
pip install ssebowa
```

If you are running this commands in colab or  jupyter notebook please use this,


```bash
!pip install ssebowa
```

Now, you can access the different models by importing them from the library:

# Ssebowa Image generation

Ssebowa-Imagen is an open-source image synthesis model that utilizes a combination of ```diffusion modeling``` and ```generative adversarial networks (GANs)``` to generate high-quality images from ```text descriptions``` and allows also to turn your few photos into ```custom model``` that is capable of generating stunning images of your ```chosen subject```. It leverages a ```100 billion dataset``` of images and text descriptions, enabling it to accurately capture the nuances of real-world imagery and effectively translate text descriptions into compelling visual representations.


## Finetuning on your own data
- Prepare about ```10-20 high-quality``` solo photos ```(jpg or png)``` like yours, friend, product or pets etc and put them in a specific directory.
- Please run on a machine with a GPU of ```16GB or more```. (If you're fine-tuning SDXL, you'll need 24GB of VRAM.)

```bash
from ssebowa import img_finetune

#initialization
data_dir = "path/images"
output_dir = "/path/models"
subject_name = "<subject name>"
class_name = "person"
```

```bash
model = img_finetune.img_finetune(data_dir=data_dir, 
                                  output_dir=output_dir, 
                                  subject_name=subject_name, 
                                  class_name=class_name)
```
```bash                                  
#Data preparation
model.prepare_data()
```
```bash
#Model training 
model.training()
```
```bash
#Model inference
model.generate_image()
```
![finetune](https://ssebowa.s3.amazonaws.com/sdimage/Finetuning+on+your+own+data_image.jpg)

## Image Generation

```bash
from ssebowa import Ssebowa_imgen
model = Ssebowa_imgen()
```

## Generate an image with the text description 

Like lets generate "A cat sitting on a bookshelf"

```bash
image = model.generate_image("A cat sitting on a bookshelf")
```
## Save the image to a file

```bash
image.save("cat_on_bookshelf.jpg")
```
![image](https://ssebowa.s3.amazonaws.com/sdimage/image_generation_1.jpg)
![image](https://ssebowa.s3.amazonaws.com/sdimage/image_generation_2.jpg)

# Ssebowa Vision Language Model

Ssebowa-vllm is an open-source visual large language model (VLLM) developed by Ssebowa AI. It is a powerful tool that can be used to understand images. Ssebowa-vllm has 11 billion visual parameters and 7 billion language parameters, supporting image understanding at a resolution of 1120*1120.


```bash
from ssebowa import ssebowa_vllm
model = ssebowa_vllm()

response =  model.understand(image_path, prompt)
print(response)
```

![image](https://ssebowa.s3.amazonaws.com/sdimage/vllm_image.jpg)

# Contact

If you have any questions or suggestions, please feel free to open an issue on GitHub or contact us at support@ssebowa.ai
