"""
This module contains general helper functions for the project
"""

# import libraries
import os
import yaml
import torch
import numpy as np


def set_seed(seed):
    """ Sets seed to ensure training is reproducible """
    torch.manual_seed(seed)
    np.random.seed(seed)


def load_config(config_file):
    """ Loads model configuration file """
    with open(config_file) as file:
        conf = yaml.safe_load(file)
    return conf


def filename(configs):
    """ Creates a readable filename convention for trained models """
    dataset_name = "demo" if configs["data_directory"] == "demo" else \
        os.path.basename(os.path.normpath(configs["data_directory"]))
    file_name = "data:{}_trans:{}-{}-{}_mod:{}-{}-{}_tr:{}-{}-{}-{}-{}-{}-{}".format(dataset_name,
                                                                                     configs["transformations"]["resize_dim"],
                                                                                     configs["transformations"]["grayscale"],
                                                                                     configs["transformations"]["normalize"],
                                                                                     configs["model"],
                                                                                     configs["z_dim"],
                                                                                     configs['output_im_resolution'],
                                                                                     configs["epochs"],
                                                                                     configs["loss_fn"],
                                                                                     configs["batch_size"],
                                                                                     configs["n_disc_updates"],
                                                                                     configs["lr"],
                                                                                     configs["beta1"],
                                                                                     configs["beta2"])
    return file_name


def save_weights(configs, generator, discriminator=None):
    """ Save GAN weights - By default only generator weights are saved """
    if generator:
        if not os.path.exists("weights/gen/"):
            os.mkdir("weights/gen/")
        fname_gen = "gen_" + filename(configs)
        torch.save(generator.state_dict(), "weights/gen/" + fname_gen)
    if discriminator is not None:
        if not os.path.exists("weights/disc/"):
            os.mkdir("weights/disc/")
        fname_disc = "disc_" + filename(configs)
        torch.save(discriminator.state_dict(), "weights/disc/"+fname_disc)