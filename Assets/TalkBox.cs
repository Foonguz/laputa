using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TalkBox : MonoBehaviour
{

    public int number;
    public int oldNumber;
    public Animator anim;

    [TextArea(3, 3)]
    public string[] talk;
    public Text texted;

    public float TalkRadius;
    public LayerMask whatIsTalk;
    public Transform TalkCheck;
    public bool talked;

    void Awake()
    {

    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.E))
        {
            if (number < oldNumber)
            {
                anim.SetBool("IsOn", false);
            }
            oldNumber += 1;
        }

        talked = Physics2D.OverlapCircle(TalkCheck.position, TalkRadius, whatIsTalk);

        if (Input.GetKeyDown(KeyCode.E) && talked)
        {
            texted.text = talk[number];
            anim.SetBool("IsOn", true);
            number += 1;
        }
       
    }
}
