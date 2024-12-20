This repository contains a Python-based image encryption and decryption tool that secures images using basic pixel manipulation techniques. By applying mathematical transformations or pixel swapping, the tool allows users to encrypt and decrypt images to protect their contents.

Features

Image Encryption: Encrypts images by manipulating pixel values. Supports operations such as mathematical transformations (e.g., addition, modulo) and pixel swapping.

Image Decryption: Restores the original image using the same key or process applied during encryption. Supports Common Image Formats: Works with various image formats, including JPEG, PNG, and BMP. Interactive User Experience: Prompts users to input file paths, encryption keys, and operations for a seamless experience.

How It Works The tool reads an input image and converts it into a matrix of pixel values. Encryption applies transformations to pixel values: Mathematical operations like addition or modulo arithmetic.

Pixel value swapping. The encrypted image is saved as an output file. Decryption reverses the transformation to restore the original image.
