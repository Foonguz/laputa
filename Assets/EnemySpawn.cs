using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemySpawn : MonoBehaviour
{
    public float spawnRadius;
    public LayerMask whatIsSpawn;
    public Transform spawnCheck;
    public bool Spawn;

    public bool once = true; 

    public GameObject enemy;
    public Transform target;
    void Update()
    {
        Spawn = Physics2D.OverlapCircle(spawnCheck.position, spawnRadius, whatIsSpawn);

        if (Spawn && once)
        {
            Instantiate(enemy, target.position, target.rotation);
            once = false;
        }
        if (!Spawn)
        {
            once = true;
        }
    }
}