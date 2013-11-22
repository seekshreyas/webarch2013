Midterm Corrections
====================

by: _Shreyas_ (`shreyas@ischool.berkeley.edu`)

## 1. Draw the DOM tree for the given html5 code
Ans:

- table
    - tr
        - th
        - th
    - tr
        - td
            - p
        - td
            - ul
                - li
                - li

## 3. Mark Semantic Meaning
Ans: Missed `<div>` as another of the semantic tags. `<div>` has a semantic meaning of layout container. 
#### Although I brought it up while discussing my answer with you, I still don't consider `<div>` to be appropriately semantic. A tag if semantic gives us some information about what it contains. `<div>` stands for division of layout. So it has no information about what it contains, just signifies how it is displayed which means it is __NOT__ semantic. It has little or no semantic meaning about what it contains. Hence there is no semantic. This is why in html5 semantic tags were created like `<section>` and `<article>`. But the thing about semantics is it is a point of perception. 
My references:
- ["Let's talk about Semantics"](http://html5doctor.com/lets-talk-about-semantics/) by Mike Robinson
- ["Our pointless pursuit of Semantic Value"](http://coding.smashingmagazine.com/2011/11/11/our-pointless-pursuit-of-semantic-value/) by Divya Manian


## 7. Write the URL that browser requests when the previous form is clicked. 
Ans:
`http://example.com/app/user/search?name=Jim%20Blomo&gender=male`

## 8. Blink
I missed putting the code inside an infinite loop for it to blink continuously.
```
el = jQuery('#blink');

while (1 > 0){
    for (i=0; i<=255; i++){
        el.css({
            'color' : 'rgba(i, 255, 255, 1)'
        });

    }
}

```

## 14. Fill in the missing words to describe TCP
Ans:

_Ordering_ : Ensures packets as read in the same order they were sent by using a __sequence number__


## 15. Mark (T)rue and (F)alse
Ans:

- DNS uses UDP : __T__
- HTTP uses DNS: __F__


## 17. Circle the headers used to ensure the data in a POST request is handled correctly.
- __Host__ should have been circled
- __Accept__ should not have been circled


## 20. Give indications that the following API is RESTful
- full path of the url is enclosed in each request related to the constraints of 
    - __client-server__ : 2 separate systems talk to each other through a well defined interface
    - __stateless__: no context is stored between requests
    - __cacheable__: clients and intermediaries can cache results
    - __layered__ : requests can go through intermediaries
    - __uniform interface__: the protocol between client and server follows the same rules regardless of specific application.
