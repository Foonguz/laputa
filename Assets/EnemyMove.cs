using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyMove : MonoBehaviour
{
    public float chaseRadius;
    public LayerMask whatIsChase;
    public Transform chaseCheck;
    public bool chase;

    public GameObject target;
    void Update()
    {
        chase = Physics2D.OverlapCircle(chaseCheck.position, chaseRadius, whatIsChase);

        if (chase == true)
        {
            transform.position = Vector3.MoveTowards(transform.position, target.transform.position, 0.01f);
        }
    }
}
