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

Diffuse surfaces reflect (scatter) light in many angles. Diffuse reflection accounts for more of the color than any other type of distribution because most objects are opaque and reflect light diffusely.
Specular surfaces reflect light at the same as the angle at which the light strikes the surface. Specular reflection gives objects a glossy or mirror-like appearance.

<p float="left">
    <img width="300" alt="Reflection, spp50, mD 10, 214 92" src="https://user-images.githubusercontent.com/64409854/205479140-5392b5b0-6b2c-4578-af91-d22acb219d7d.png"> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <img width="300" alt="Reflection, spp50, mD10, 290 37" src="https://user-images.githubusercontent.com/64409854/205479037-35c43306-273e-4131-83c3-f4b0227ca504.png">
    
</p>
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 214.92 sec &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 290.37 sec

## **Glossy Reflections** 
Glossy surfaces are actually specular surfaces with micro surfaces at angles to surface plane. These micro surfaces reflect light not only specularly but also diffusely (at angles very close to the specular transmission), giving the surface a glossy appearance.

<img width="300" alt="Glossy, spp50, mD10, 289 50" src="https://user-images.githubusercontent.com/64409854/205715261-f48bc269-2df4-4acf-97f4-51c99bef66a4.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 280.50 sec


## **Refractions**
Refractions occur when rays intersect refractive spheres. The light at the intersection point is determined by blending the reflected and refracted light at that point. A reflective ray is cast in the same way as described in the previous section. The refractive ray is calculated by bending the original ray based on the angle of incidence and the indices of refraction of the two materials. The amount of reflective and refractive light at the point is determined by the Fresnel equation.

<img width="300" alt="Refractions, spp50, mD10, 62 05" src="https://user-images.githubusercontent.com/64409854/205715307-5336a3ba-ea5c-4ef2-853a-69cf0756ee94.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 62.05 sec

## **Shadows**

Shadows are incorporated into lighting. To determine if a light source should contribute to the lighting at an intersection point a shadow ray is cast from the intersection point to the light source. If there is an intersection before the light source then this point is in the shadow of that light source.  
<p>
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
    Hard Shadows &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    Soft Shadows
</p>
<p>
    <img width="300" alt="Hard_Shadow 63 19" src="https://user-images.githubusercontent.com/64409854/205715373-917539a5-3ff5-4faf-b474-7ffeb2652c55.png">       &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <img width="300" alt="Soft_Shadow 154 62" src="https://user-images.githubusercontent.com/64409854/205715390-b1e0e02b-30b3-4dfa-8e7b-bb8620c8ad56.png">
</p>          
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 63.19 sec &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 154.62 sec

## **Spotlight**
A spotlight produces a directed cone of light. The light becomes more intense closer to the spotlight source and to the center of the light cone.

<img width="300" alt="SpotLight 115 55" src="https://user-images.githubusercontent.com/64409854/205715652-5511fe6a-8219-4aba-9fe4-592d464cf1e2.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 115.55 sec

## **Image Textures** 
Uniformly colored 3D objects look nice enough, but they are a little bland. Their uniform colors don't have the visual appeal of, say, a brick wall or a plaid couch. Three-dimensional objects can be made to look more interesting and more realistic by adding a texture to their surfaces.
An image texture can be applied to a surface to make the color of the surface vary from point to point, something like painting a copy of the image onto the surface.

<img width="300" alt="Space 172 13" src="https://user-images.githubusercontent.com/64409854/205715658-3ff659a3-220c-4792-98de-24aa398e6f58.png">
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 172.13 sec

## **Normal Mapping**
Normal Mapping, or Bump Mapping, is a texture mapping technique used for faking the lighting of bumps and dents – an implementation of bump mapping. It is used to add details without using more polygons. A common use of this technique is to greatly enhance the appearance and details of a low polygon model by generating a normal map from a high polygon model or height map.

<p>
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    Without Normal Mapping
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    With Normal Mapping
</p>
<p>
    <img width="300" alt="Without NM 84 19" src="https://user-images.githubusercontent.com/64409854/205993789-5b288ad6-1df0-45b1-b1bf-c784a69e72a1.png">
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <img width="300" alt="With NM 100 87" src="https://user-images.githubusercontent.com/64409854/205994007-ea817d1e-444c-4659-a29d-4dd262e307be.png">
</p>

SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 84.19 sec &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 100.87 sec


<p>
    <img width="300" alt="Normal_Mappings 148 93" src="https://user-images.githubusercontent.com/64409854/205987730-9d181048-09af-4fc1-bcd2-2019ba37497e.png">
</p>
SPP: 50 &nbsp Depth:10 &nbsp Time Taken: 148.93 sec
