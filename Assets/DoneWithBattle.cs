using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoneWithBattle : MonoBehaviour
{

    public GameObject player;
    public GameObject location;

    public float TeleportRadius;
    public LayerMask whatIsTele;
    public Transform TeleCheck;
    public bool gone;

    public bool done;

    void Update()
    {
        gone = Physics2D.OverlapCircle(TeleCheck.position, TeleportRadius, whatIsTele);

        if(gone)
        {
            done = true;
        }
        if(!gone && done)
        {
            player.transform.position = location.transform.position;
            done = false;
        }
    }
}
