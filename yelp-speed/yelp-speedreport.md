HW7 :: Yelp Speed Report
=========================

Author: __Shreyas__

Email: __shreyas[at]ischool.berkeley.edu__

## Yelp Speed Report

#### What’s the difference between Yelp’s homepage compressed and uncompressed?

I used `curl` command to gather statistics on yelp homepage download. 
```
$ curl --url www.yelp.com --header "Accept-Encoding:[ENCODING VALUE];q=1.0" > yelp-[ENCODING]
```

The following encoding values were used:

- `*` : Any available encoding supported by the server
- `deflate`: No compression
- `compress` : UNIX _compress_ method (deprecated in most browsers).
- `gzip`: GNU Zip format
- `bzip2`: lossless compression
- `lzma`: LZMA compression (which apparently has more compression ratio than gzip)[^note-1]
- `sdch`: Google's new __Shared Dictionary Compression for HTTP__ [^note-2]

And also I observed and rechecked the values as we get in our browsers- Safari, Mozilla, Chrome.

Their values were noted down __after clearing the browser cache and cookies__. 

Also `q=1.0` was used as default, which might not have been required, as there was only 1 value in the encoding.


| Compression | FileSize | Download speed (via Curl) |
|:------------|---------:|-------------------------:|
| `*` | 93K | 124k | 
| `deflate` (uncompressed) | 95K | 215k |
| `bzip2` | 84K | 99k |
| `compress` (deprecated) | 93K | 125k |
| `gzip` | 18K | 42k |
| `lzma` | 87K | 135K |
| `sdch` | 89K | 98k |
| `Chrome-Compressed` | 20.8K | - |
| `Chrome-Uncompressed` | 91.9K | - |
| `Firefox-Compressed` | new firefox tool doesn't give compressed file size | - |
| `Firefox-Unompressed` | 92.13 K | - |
| `Safari-Compressed` | safari tool doesn't give compressed file size | - |
| `Safari-Uncompressed` | 85.59 K | - |


[^note-1]: [HTTP Compression on Wikipedia](http://en.wikipedia.org/wiki/HTTP_compression)

[^note-2]: [RFC 3248](http://tools.ietf.org/html/rfc3284)