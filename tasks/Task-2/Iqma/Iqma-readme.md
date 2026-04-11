## My learning Take-aways

### General
Computers can’t actually see the robot or know how it is, it only understands numbers. Forward kinematics is measuring from where the robot is to where it needs to reach, by taking each angle and calculating the positions the robot will end up in with those angles. Inverse kinematics takes the positing we need to get to first, then tries to calculate it backwards to what angle it would be.

- each link has to be fully defined(all parameters plane, length, angles, constraints?)

### 2d links

we used basic trigonometry, translated graphs to equations

End-Effector E(x₂, y₂)
              ●
             /
            /L₂
           /
    Joint ●
         /
        /L₁ 
       /
Base  ●────────► X-axis
      │
      ▼

### 3d links
#### Transformation matrix
We use matrix cause its hard to track 3d spaces with equations alone and we can't properly map it out without matrix. used corresponding angles postulate at some point,forgot about that rule, but was able to map it to alternate angles in a way, then I drew it out to confirm all angle relations that led to the law(drawing a diagonal in the middle basically makes it easier).

We used transformation matrix to convert the matrix equation into a single matrix (added 0 0 1 to make it complete? - research why later, or check school notes i guess)

Transformation = rotation + translation

*Been wondering why we even needed to map E(end effector) back to 0(origin) in the first place, I've decided its because we need it to calculate the inverse kinematics(remember the example of describing the location of an object to your friend from your own frame since his frame is different, yeah that sums it up)*
```  
                __
End Effector E  \
               ● \__
              /
             /L₂
            /
   Joint A ●
          /
         /L₁ 
        /
Base 0 ●────────► X-axis
      │
      ▼
```

So, we first transformed A to 0, then E to A, then multiply both together to get E to 0.

<sup>o</sup><sub>A<sub>T = ----                  ----      
                           | cos0₁ -sin0₁  L₁ cos0₁ |
                           | sin0₁  cos0₁  L₁ sin0₁ |
                           ----                  ----

<sup>A</sup><sub>E<sub>T = ----                  ----      
                           | cos0₂ -sin0₂  L₂ cos0₂ | (not 0₁ + 0₂ cause this is)
                           | sin0₂  cos0₂  L₂ sin0₂ | (just to A and not to origin)
                           ----                  ----

so after multiplying we have
<sup>o</sup><sub>E <sub>T = ----                  ----      
                           | cos0₁ -sin0₁  L₁ cos0₁ |
                           | sin0₁  cos0₁  L₁ sin0₁ |
                           ----                  ----
remember that it differs based on matrix parameters (multiplying a 2x2 matrix by a 2x1 is different from multiplying a 3x3 by a 3x3)       

[Link to class recording](https://www.youtube.com/watch?v=pMIFt7OhBFY&list=PL0vKqkgonPB4eaz1xtSsuH4O1duWuI1sg&index=14&t=2s) in case you need to go over the calculations again (you probably will)

 
 ## ITK diaries

 