using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;
public class level5controller : EventTrigger {

	// Use this for initialization
	public void OnBeginDrag(PointerEventData data)
    {

    }
    public override void OnDrag(PointerEventData data)
    {
        Vector3 worldSpaceMousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);

        Vector3 canvasMousePos = transform.parent.InverseTransformPoint(worldSpaceMousePos);

        transform.localPosition = new Vector3(
            canvasMousePos.x,
            canvasMousePos.y,
            transform.localPosition.z
            );

    }
}
