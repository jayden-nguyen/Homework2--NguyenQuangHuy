using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class predictNumber : MonoBehaviour {
    //declare UI variables
    public Text title;
    public Text content;
    public Button lower;
    public Button yes;
    public Button higher;
    public InputField range;
    int min;
    int max;
    int temp;
	// Use this for initialization
	void Start () {
        content.text = "Please input min and max (input in form \"min-max\")";
	}
	
	public void getInput()
    {
        char de = '-';
        string[] test = range.text.Split(de);
        min = int.Parse(test[0]);
        max = int.Parse(test[1]);
        range.text = "";
        content.text = "please think a number between " + min.ToString() + " and " + max.ToString();
        range.gameObject.SetActive(false);
        temp = Random.Range(min, max);
        content.text = "Is the number " +  temp + " ? ";
    }
    public void Lower()
    {
        max = temp;
        temp = Random.Range(min, max);
        content.text = "Is the number " + temp + " ? ";
    }
    public void Higher()
    {
        min = temp;
        temp = Random.Range(min+1, max);
        content.text = "Is the number " + temp + " ? ";
    }
    public void Yes()
    {
        content.text = "yes, I win";
    }
	
}
