﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class startScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
    public void LetGo()
    {
        SceneManager.LoadScene(1);
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
