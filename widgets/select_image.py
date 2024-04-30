from glob import glob
from pandas import DataFrame
from streamlit import sidebar
from enum import Enum


class Option(Enum):
    Samples = "Use Sample Images"
    Upload = "Use upload Image"


def select_image():
    option = sidebar.radio("What option do you use?",
                           (Option.Samples.value, Option.Upload.value))

    sample_images = glob('*[.jpg][.jpeg][.png][.gif]')
    sample_images_date_frame = DataFrame(sample_images, columns=['Images'])
    image_selected = sidebar.selectbox('Choose a sample image',
                                       sample_images_date_frame['Images'])

    image_uploaded = sidebar.file_uploader(label="Upload your own Image")

    if option == Option.Samples.value:
        image = image_selected
    elif option == Option.Upload.value and image_uploaded is not None:
        image = image_uploaded
    else:
        image = image_selected

    sidebar.image(image)

    return image
