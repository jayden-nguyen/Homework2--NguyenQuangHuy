using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
public class level4script : MonoBehaviour
{
    public Text levelText;
    public Text hinText;
    public Image hint2Image;
    public string levelContent = "LEVELS";
    public string levelNumber;
    public InputField inputField;
    public Button submitButton;
    public string levelAnswer;
    public GameObject barObject;
    public int count = 0;
    string answer;
    // Use this for initialization
    void Start()
    {
        levelText.text = levelContent;
        StartCoroutine(ChangeLevelTextRoutine());
        hint2Image.gameObject.SetActive(false);
    }
    public void GetInput()
    {
        answer = inputField.text;
        CheckAnswer(answer.ToLower());
    }
    public void GetHint()
    {
        count++;
        if (count % 2 == 1)
        {
            hint2Image.gameObject.SetActive(true);
            barObject.gameObject.SetActive(false);
        }
        else
        {
            hint2Image.gameObject.SetActive(false);
            barObject.gameObject.SetActive(true);
        }


    }

    public void CheckAnswer(string answer)
    {
        if (answer == levelAnswer)
        {
            hinText.text = "Yayyyy";
            //TODO: Change scene
            SceneManager.LoadScene(5);
        }
        else
        {
            hinText.text = "WRONGGGG!!!!!";
            hinText.color = Color.red;
            inputField.text = "";
            inputField.ActivateInputField();
        }
    }
    IEnumerator ChangeLevelTextRoutine()
    {
        while (true)
        {
            levelText.text = levelContent;
            //Wait for 2 seconds
            yield return new WaitForSeconds(2f);
            levelText.text = levelNumber;
            yield return new WaitForSeconds(2f);
        }

    }
    // Update is called once per frame
    void Update()
    {

    }
}

