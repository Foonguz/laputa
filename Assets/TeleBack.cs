using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TeleBack : MonoBehaviour
{

    public GameObject player;
    public GameObject playerTeleBack;

    public void Activate()
    {
        playerTeleBack.transform.position = player.transform.position;
    }
}
