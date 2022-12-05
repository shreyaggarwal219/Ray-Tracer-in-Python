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
<img width="300" alt="Specular_Lighting, 39 14" src="https://user-images.githubusercontent.com/64409854/205715174-7ee7bf00-a7cf-40fa-9a42-d43f6a265953.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 39.14 sec

## **Reflections**
Reflections are performed by casting rays originating from the intersection point directed along the reflection vector. A portion of the reflected ray's color will be contributed to the original intersection point based on how reflective the surface is. Fortunately this is fairly easy given the a recursive approach for casting rays. There is an arbitrary limit on how many reflections a ray can perform before stopping to improve performance and eliminate potential infinite loops.

<p float="left">
    <img width="300" alt="Reflection, spp50, mD 10, 214 92" src="https://user-images.githubusercontent.com/64409854/205479140-5392b5b0-6b2c-4578-af91-d22acb219d7d.png">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <img width="300" alt="Reflection, spp50, mD10, 290 37" src="https://user-images.githubusercontent.com/64409854/205479037-35c43306-273e-4131-83c3-f4b0227ca504.png">
    
</p>
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 214.92 sec &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 290.37 sec

## **Glossy Reflections** 
<img width="300" alt="Glossy, spp50, mD10, 289 50" src="https://user-images.githubusercontent.com/64409854/205715261-f48bc269-2df4-4acf-97f4-51c99bef66a4.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 280.50 sec


## **Refractions**
Refractions occur when rays intersect refractive spheres. The light at the intersection point is determined by blending the reflected and refracted light at that point. A reflective ray is cast in the same way as described in the previous section. The refractive ray is calculated by bending the original ray based on the angle of incidence and the indices of refraction of the two materials. The amount of reflective and refractive light at the point is determined by the Fresnel equation.

<img width="300" alt="Refractions, spp50, mD10, 62 05" src="https://user-images.githubusercontent.com/64409854/205715307-5336a3ba-ea5c-4ef2-853a-69cf0756ee94.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 62.05 sec
## **Shadows**
Shadows are incorporated into lighting. To determine if a light source should contribute to the lighting at an intersection point a shadow ray is cast from the intersection point to the light source. If there is an intersection before the light source then this point is in the shadow of that light source.
<p>
    <img width="300" alt="Hard_Shadow 63 19" src="https://user-images.githubusercontent.com/64409854/205715373-917539a5-3ff5-4faf-b474-7ffeb2652c55.png">
    <img width="300" alt="Soft_Shadow 154 62" src="https://user-images.githubusercontent.com/64409854/205715390-b1e0e02b-30b3-4dfa-8e7b-bb8620c8ad56.png">
</p>
## **Spotlight**
A spotlight produces a directed cone of light. The light becomes more intense closer to the spotlight source and to the center of the light cone.
<img width="605" alt="SpotLight 115 55" src="https://user-images.githubusercontent.com/64409854/205715652-5511fe6a-8219-4aba-9fe4-592d464cf1e2.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 115.55 sec

## **Image Textures** 
<img width="601" alt="Space 172 13" src="https://user-images.githubusercontent.com/64409854/205715658-3ff659a3-220c-4792-98de-24aa398e6f58.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 172.13 sec




