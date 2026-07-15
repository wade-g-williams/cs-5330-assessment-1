# cs-5330-assessment-1

### Assessment \#1: Classical Vision Topics
 
This is the first assessment. Each assessment will be a creative activity that involves teaching a small topic in computer vision. For the first assessment, the topics will be related to material covered in class during the first five weeks.
 
The topic assignment is [here](https://docs.google.com/spreadsheets/d/1zTzRs5XvBBxWpUlYXhLlV2D7xHIC-KV-D7Ko-OPin6g/edit?usp=sharing)
 
[Links to an external site.](https://docs.google.com/spreadsheets/d/1zTzRs5XvBBxWpUlYXhLlV2D7xHIC-KV-D7Ko-OPin6g/edit?usp=sharing)
 
. Each person has two randomly assigned topics. Choose only one of them for your assessment.
 
For this assessment you will create a video that is 8-12 minutes in length (10min should be your target). The goal of the video is to teach one of your two assigned topics. Your audience is students who are in a computer vision course. You should place your assigned topic within the context of this course and the topic orderings of my [outlines](https://northeastern.instructure.com/courses/253587/files/41982438?wrap=1)
 
[Download outlines](https://northeastern.instructure.com/courses/253587/files/41982438/download?download_frd=1)
 
. You can assume your audience knows material that came before your topic. 
 
For a few of the topics, there are two of you with the same potential topic. You need to create your own materials and video for your own topic, but you may collaborate with the other person with your topic to better understand it. You may also collaborate (closely) with people who are doing topics that come before or after your own topic, with the goal of minimizing overlap and building on prior topic presentations. I've put the topics in (mostly) course-order below so you can see where your topic sits within that context. There may be related topics that are a bit earlier or later.
 
We will evaluate your videos based on the following criteria.
 
* Slides: clarity of expression  
* Slides: quality of examples/diagrams/figures  
* Presentation: correctness  
* Presentation: clarity of the explanation  
* Presentation: quality of examples chosen for the purpose of teaching  
* Presentation: you introduce yourself and your topic  
* Presentation: make good use of your time and stay within the specified time limit  
* Presentation: the presentation aligns with and doesn't overlap significantly with related topics  
* Submission: includes a link to your video, a pdf of your slides, and a readme with your name, a reflection, and acknowledgement that includes how (if) you used an LLM
If you have any questions about your topic, please post to Piazza. If you feel like you can't fit it into the time limit, ask for assistance in cutting down what you need to present. If you feel like your topic is too short, ask for assistance in how to come up with examples or perhaps add a strongly related topic not on the list.  Your overall video should be within the specified time window.
 
Note, you do not have to use slides, but you need to use some type of visual aid. If you use an electronic white board/notebook of some kind, that's fine. Please submit your final white boards as a pdf in place of slides.
 
---
 
### Submission
 
Please submit to Gradescope a link to your video (in your readme or reflection), a pdf of your slides, and a readme with your name, a reflection, and an acknowledgement of the resources you used. The acknowledgement should include how (if) you used an LLM as part of the process and whether you collaborated with anyone else. While use of an LLM is not prohibited, I recommend using it as a learning aid rather than a replacement for cognitive tasks.
 
**Optional**: as I mentioned in class, I'm thinking about making a non-commercial YouTube channel with the vision tutorials on it.  If you would like to have your video posted on it, please include that in your readme file. It is completely optional and will have no impact on your grade.
 
---
 
### Topics in Course Order
 
1. concepts: Overview of computer vision versus image processing  
2. physics: Explaining visible light and surrounding regions, definitions of wavelength/frequency  
3. biology: Overview of human visual system: definition and organization of the parts  
4. biology: Distribution of cones and rods in the human eye, relevance to computer vision  
5. biology: High level overview of Hubel and Weisel's work on the visual cortex in cats: neurons respond to simple features in the visual feidl  
6. biology: High level overview of Margaret Livingstone's work showing a higher resolution mostly luminance pathway and lower resolution mostly color pathway.  
7. concepts: Overview of a machine vision system: definition and organization of the parts  
8. physics: Explanation of how a lens focuses light, what is the focal length?  
9. sensing: CCD (charge-coupled device)  
10. sensing: 3-CCD color cameras  
11. sensing: CMOS sensor  
12. sensing: Explanation of RGB filters overlaid on the visible spectrum  
13. sensing: Explanation of the Bayer pattern, why 2 green?, variations on the basic pattern  
14. sensing: a Bayer interpolation algorithm  
15. physics: Pinhole camera model, projection diagram, perhaps some historical context and practical uses, concept of the image plane sitting in front of the camera v. sensor sitting behind.  
16. physics: Deriving the perspective projection equation from the pinhole camera model and the image plane  
17. physics: Estimating time to collision using the perspective projection equation and apparent size  
18. physics: Presenting the thin lens model, the intuition provided by it, and the limits it puts on focusing on near objects  
19. physics Giving a few examples of using the thin lens model, and talking about it as potentially permitting depth from focus  
20. physics: An explanation of the concept of depth of field and the factors that affect it.  
21. memory: Storing images in memory: converting a 2-D block into 1-D, interleaved versus planar, row-major versus column-major and why it is important  
22. Correlation: explained with a 1-D example, analog and discrete  
23. Correlation: explained with a 2-D example, discrete only  
24. Convolution: explained with a 1-D example, analog and discrete  
25. Convolution: explained with a 2-D example (discrete, not analog)  
26. Convolution: handling boundaries, valid, same, full and when to use each one  
27. Convolution: handling boundaries, zero-padding, reflection, custom filter sizes and usage cases for each one  
28. Convolution: associativity and separable filters  
29. Useful filters: a discrete Gaussian, with a simple example, divisor  
30. Useful filters: a continuous Gaussian, choosing the standard deviation  
31. Useful filters: Sobol X and Sobol Y application, purpose, and conversion to magnitude and orientation (visualizations)  
32. Useful method: Non-maxima suppression in the context of gradient magnitude and orientation  
33. Useful filters: Laplacian and the difference of Gaussians approximation  
34. Useful filters: Median filter, example of removing salt and pepper noise / edge preserving  
35. Useful filters: Bilaterial filter  
36. Useful filters: Laws Filters  
37. Useful filters: Gabor Filters  
38. FT: concept of signals as a collection of simple sines and cosines  
39. FT: computational complexity of the Fast Fourier Transform and convolution in spatial v. frequency domain  
40. FT: representing the Fourier Transform as an image: how to understand a 2-D FT  
41. FT: how to create low-pass or high-pass filters in the Fourier domain  
42. ANN: a basic node in an artificial neural network  
43. ANN: types of non-linear functions used in ANNs and CNN  
44. ANN: what is a convolution layer in a CNN?  
45. ANN: What are the key parameters of a convolution layer in a CNN? filter size, channels, stride, non-linear function  
46. ANN: what is a pooling layer in a CNN?  
47. ANN: how do you compute the number of parameters for a convolution layer, how does it compare to a fully-connected layer?  
48. ANN: concept of a convolution stack, give a simple example  
49. ANN: idea of activations at each layer representing an embedding of the image, how that embedding changes within the conv stack  
50. color spaces: explain sRGB and why it was creaetd  
51. color spaces: explain YIQ and YUV and their relation to human perception  
52. color spaces: explain HSV and how it might be/is used  
53. color spaces: explain XYZ and its relation to human perception and its utility in perception studies  
54. color spaces: explain CIE-Luv and CIE-Lab and their intent and appropriate uses  
55. color spaces: explain what chromaticity spaces are (2-D color spaces) and give some examples  
56. histograms: explain and give an example of a 1D histogram (e.g. a greyscale image)  
57. histograms: explain and give an example of a 2D chromaticity histogram  
58. histograms: explain how to think about a 3D color histogram  
59. histograms: explain how histograms can be considered a probability distribution if you normalize them, what does it tell you about an image?  
60. histograms: explain SSD and histogram intersection as distance metrics for histograms (expand to include earth mover's distance, if time allows)  
61. Thresholding: explain the concept and give an example (e.g. green screen)  
62. Distance metrics: explain the L-N norms, focusing on L-1, L-2 and L-infinity as examples  
63. Features: Entropy, what are some uses in computer vision?  
64. Texture: what is texture, why does it have to be an area feature (we can't calculate it at a single pixel)  
65. Texture: computing a texture feature using Laws filters  
66. Texture: computing a texture feature using Gabor filters  
67. Texture: Varma and Zisserman method using a filter bank  
68. Texture: Varma and Zisserman method using plain pixel values  
69. Kmeans: K-means clustering algorithm  
70. Kmeans: using K-means to build a code book, for example to identify 256 colors for a GIF  
71. File types: explain the key file types and their different qualities/uses  
72. Aliasing: What is aliasing (basic concept)  
73. Aliasing: explain spatial aliasing and find an example  
74. Aliasing: explain temporal aliasing and find an example  
75. Aliasing: what is the best solution to aliasing (remove high frequencies before sampling)  
76. PCA: basic eigenvector/eigenvalue concept  
77. PCA: process for principal components analysis  
78. PCA: analyzing how many significant dimensions are in the data / picking the number of eigenvectors to keep  
79. PCA: concept of an eigenspace, how to project something into an eigenspace  
80. PCA: how to go from a point in the eigenspace back to the original data space  
81. PCA: how to generate an eigenspace for a set of objects (e.g. Murase and Nayar method)  
82. PCA: how we might use PCA to visualize a high dimensional space, such as the embeddings of a CNN  
83. DNN: What is a global average pooling layer (e.g. last layer of a ResNet18 conv stack)  
84. DNN: Concept of an embedding and how we can use it for matching images  
85. DNN: distance metrics for embeddings (SSD, and cosine distance), how are they conceptually different?  
86. bip: concept of 4-conn and 8-conn processing in binary image processing with examples of how they cause different results  
87. bip: growing (dilation) and shrinking (erosion)  
88. bip: closing and opening and combinations of dilation and erosion  
89. bip: grassfire transform and how it can make closing/opening faster  
90. region features: moments, include Hu moments if time allows  
91. region features: computing axis of least central moment, the oriented bounding box, h/w ratio and % filled  
92. segmentation: region growing (DFS) to identify all connected components in an image  
93. segmentation: concept of the normalized cut versus minimum cut and why it is useful for segmentation  
94. appearance models: dichromatic reflection model, explanaton of body reflection and surface/interface reflection  
95. appearance models: bi-illuminant dichromatic reflection model, how is it different, what are the insights it enables
