using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{
    public Rigidbody2D rb;
    public float x; 
    public float y;
    public float speed;
    void FixedUpdate()
    {
        if (Input.GetKey(KeyCode.A))
        {
            x =+ speed * -1;
        }

        else if (Input.GetKey(KeyCode.D))
        {
            x =+ speed;
        }
        else
        {
            x = 0;
        }

        if (Input.GetKey(KeyCode.S))
        {
            y =+ speed * -1;
        }   
        else if (Input.GetKey(KeyCode.W))
        {
            y =+ speed;
        }
        else
        {
            y = 0;
        }

        rb.velocity = new Vector2(x * speed, y * speed);

    }

}
