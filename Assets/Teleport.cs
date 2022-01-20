using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Teleport : MonoBehaviour
{
    public GameObject player;
    public GameObject location;

    public TeleBack teleBack;

    public float TeleportRadius;
    public LayerMask whatIsTele;
    public Transform TeleCheck;
    public bool gone;

    public bool hasTeleported; 
    void Start()
    {

    }
    void Update()
    {
        gone = Physics2D.OverlapCircle(TeleCheck.position, TeleportRadius, whatIsTele);

        if (gone)
        {
            teleBack.Activate();
            player.transform.position = location.transform.position;
            hasTeleported = true; 
        }

        if(gone && hasTeleported)
        {
            Destroy(gameObject);
        }
        
    }

}
