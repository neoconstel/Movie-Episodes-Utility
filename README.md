# Movie Episodes Utility
Solves issues of missing or unordered episode filenames.

## More Detailed Summary
Sometimes you collect tons of movie episodes from someone, and it turns out 
the filenames are badly named using different naming conventions. This makes 
it difficult to sort the filenames accordingly to locate the ones you need at 
the moment. To handle this issue, the renaming functionality is provided to 
quickly rename all the episodes into a standard format with a desired title 
as the prefix.

Also, sometimes the filenames might or might not be orderly-named but they are 
too many and some are missing. How do you quickly know which ones are missing 
so you can decide to make a suitable resolution to the problem immediately, 
such as re-downloading them using the public WiFi in the restaurant you're 
currently eating at before heading back home? 
Well, that's why the missing episodes functionality is here to help.

## Features Implemented
- Episode Renaming (includes support for undoing the previous renaming 
performed within the specified directory)
- Missing Episodes Reporting
- GUI Interface

## Requirements to Launch
- Just have python (3.6+) installed. No extra modules/packages are needed.

## Installation
#### Linux
- Clone this repository to anywhere on your PC.
- Open your terminal within the cloned repository and run __sudo ./setup.sh__
- Grant install access by inputting your password when asked to.
- Finally with it installed, launch the software with __episode-utility__

> Note that you should launch it from the directory containing the episodes you 
wish to operate on. For instance if your Samurai-X episodes are in the directory: 
__/home/zoro/anime/samurai-x__, you should navigate to 
__/home/zoro/anime/samurai-x__ in your terminal and run __episode-utility__ 
from there.

#### Windows
Currently there is no installation made for windows. I intend to, but if 
anyone is in immediate need of it kindly reach out to me and I'll make it a 
priority. Thanks, and happy watching! 😀
