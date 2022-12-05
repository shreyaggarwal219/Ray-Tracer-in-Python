# Ray-Tracer-in-Python
## **Introduction**  
This is a simple Ray Tracer which supports Diffuse Lighting, Phong Lighting, Blinn Lighting,
Lambert Material, Metal Material, Dielectric Material, Glossy Material, Directional Lights, Point Lights,
Spotlights, Hard and Soft Shadows, Super Sampling, Positionable Camera.     
The Geometric Primitives supported are Spheres and Axis Aligned Planes.  
The Ray Tracer uses Bounding Volume Hierarchies as the main Acceleration Structure.

## **Diffuse Lighting**
Diffuse lighting is determined by computing the intensity of the light at a point on the sphere. If the angle is close to the normal at that point then the intensity will be increased. The intensity determines how much of the object's color to contribute.

<img width="300" alt="DiffuseLighting, spp50, md10, 38 55" src="https://user-images.githubusercontent.com/64409854/205715029-cddd84c0-64cf-4502-bdde-ffef088fe00b.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 38.55 sec

## **Specular Lighting**
Specular lighting is calculated by computing a reflection ray by reflecting the light vector about the normal at the intersection point. The view ray is compared to the reflection ray to determine how much specular lighting to contribute. The more parallel the vectors are the more specular lighting will be added.

## **Reflections**
Reflections are performed by casting rays originating from the intersection point directed along the reflection vector. A portion of the reflected ray's color will be contributed to the original intersection point based on how reflective the surface is. Fortunately this is fairly easy given the a recursive approach for casting rays. There is an arbitrary limit on how many reflections a ray can perform before stopping to improve performance and eliminate potential infinite loops.

<p float="left">
    <img width="300" alt="Reflection, spp50, mD 10, 214 92" src="https://user-images.githubusercontent.com/64409854/205479140-5392b5b0-6b2c-4578-af91-d22acb219d7d.png">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <img width="300" alt="Reflection, spp50, mD10, 290 37" src="https://user-images.githubusercontent.com/64409854/205479037-35c43306-273e-4131-83c3-f4b0227ca504.png">
    
</p>
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 214.92 sec &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 290.37 sec

## **Glossy Reflections** 



## **Refractions**
Refractions occur when rays intersect refractive spheres. The light at the intersection point is determined by blending the reflected and refracted light at that point. A reflective ray is cast in the same way as described in the previous section. The refractive ray is calculated by bending the original ray based on the angle of incidence and the indices of refraction of the two materials. The amount of reflective and refractive light at the point is determined by the Fresnel equation.

## **Shadows**
Shadows are incorporated into lighting. To determine if a light source should contribute to the lighting at an intersection point a shadow ray is cast from the intersection point to the light source. If there is an intersection before the light source then this point is in the shadow of that light source.

## **Spotlight**
A spotlight produces a directed cone of light. The light becomes more intense closer to the spotlight source and to the center of the light cone.

## **Image Textures** 





