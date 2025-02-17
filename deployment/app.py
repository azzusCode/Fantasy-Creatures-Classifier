from fastai.vision.all import *
import gradio as gr

fantasy_creatures = (
    'Angel', 'Basilisk', 'Centaur', 'Chimera', 'Cyclops', 'Demon', 'Dragon', 'Dwarf', 'Elf', 'Fairy', 
    'Fire Elemental', 'Genie', 'Ghost', 'Goblin', 'Golem', 'Griffin', 'Hydra', 'Kraken', 'Lich', 'Mermaid', 
    'Minotaur', 'Orc', 'Pegasus', 'Phoenix', 'Unicorn', 'Water Elemental', 'Werewolf', 'Wizard', 'Wraith', 'Zombie'
)

model = load_learner("models/creatures-classifier-v2.pkl")

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(fantasy_creatures, map(float, probs)))

image = gr.Image()
label = gr.Label(num_top_classes=5)
examples = [
    'test_images/image1.jpg',
    'test_images/image2.jpg',
    'test_images/image3.jpg',
    'test_images/image4.jpg',
    'test_images/image5.jpg'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)
