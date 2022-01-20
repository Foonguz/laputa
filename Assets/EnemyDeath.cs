using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyDeath : MonoBehaviour
{
    public float bulletRadius;
    public LayerMask whatIsBullet;
    public Transform bulletCheck;
    public bool hit;

    void Update()
    {
        hit = Physics2D.OverlapCircle(bulletCheck.position, bulletRadius, whatIsBullet);

        if (hit)
        {
            Destroy(gameObject);
        }
    }
}
