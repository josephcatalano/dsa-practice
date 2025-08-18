**Aug 17 2025**

GIT
    git init - creates subfolder named .git this folder is the brain of your repo.  Its where git tracks every change and stores history. (do this for every project)
    git add <file> - moves the files into a waiting room called "Staging Area". Multiple files are added before a commit then push. 
    git push <file> - This is when you upload that photo from your camera roll to your online gallery (GitHub) to share it.
    git pull <file> - You do this every day on a repository you already have. It checks the remote for new commits and downloads them to your existing local copy. It's like getting today's issue of the magazine in the mail.
    git commit - This is when you actually press the shutter button. You take the snapshot and give it a description (a commit message). The photo is now saved in your local camera roll (your local repository).
        -m "<message>" (Message Flag)
    git add <file> - This is like arranging the scene and deciding what's going to be in the picture. You are "staging" the shot.
    .gitignore - stores all the files you don't want to track (ex. don't save the .venv because it can be very large and specific to each dev's computer)
    git remote add origin <your-repository-url.git> - Connects local repo to the new remote one on GitHub
    git push -u origin main - Send local commit history up to GitHub
    git clone <paste-github-url-here> - You do this once per machine to create a brand new, local copy of a remote repository. It's like subscribing to a new magazine; you get the entire back-catalog and are set up for future issues.
    git diff --staged - compare the snapshot of files you created with git add (shows everything you have added)
    git log - Shows list of commit history starting with most recent

PIP
    pip freeze > requirements.txt - Generates a list of installed packages, and then pours them into a new file called requirements.txt
    pip install -r requirements.txt - Tells pip to install everything in your requirements file.



VENV
    python -m venv .venv - create a virtual environment inside your project folder (Always do this when making new project)
    (WIN) .venv\Scripts\activate - Activate the venv, once its activated any package you install with pip will go only inside the isolated environment
    (MAC) source .venv/bin/activate 
    - resolves any conflict between different versions of packages (pandas 1.5 & pandas 2.0)
    - Create and "activate" a venv for "DSA Project"
    - inside it you install only the packages that project needs
    - the requirements.txt file is then generated from inside this environment, so it only lists the specific packages for that project


BIG O NOTATION (How code slows as data grows)
    - Formal way to describe how the resources required by an algorithm are affected by the size of its input. 
    - Big O doesn't measure performance in seconds but measures the Rate Of Growth of the number of operations.
    - Big O answers the question "As the input to my algorithm gets bigger, how much longer will it take to run?"

    O(1) - Constant Time
        - The amount of data does not matter algorithm will be completed in the same amount of steps
        EX. "Get me the 3rd item in the list" (my_list[2]), doesn't matter how big the list is the amount of work stayed constant
    
    O(log n) - Logarithmic Time
        - As the amount of data increases the amount of steps increases but by a less amount as the data increases (more data there is more efficient it becomes)
        Ex. binary search

    O(n) - Linear Time
        - As the amount of data increases the amount of steps increase by the amount of data (n).
        Ex. a four loop that iterates over 10 numbers in a list vs a four loop that iterates over 1000000 numbers in a list

    O(n log n) - Quasilinear Time
        - As the amount of data increases the amount increases but by a larger amount as the data increase (more data there is less efficient it becomes)
        Ex. Quicksort, Mergesort, Heapsort

    O(n^2) - Quadratic Time
        - As the amount of data increases the number of steps increases by n*n operations. 1 operation for 1 item, 4 operations for 2 items, 9 operations for 3 items. 
        Ex. Intersection sort, Selection sort, Bubblesort

    O(n!) - Factorial Time
        - As the amount of data increases the number of steps increases by a factorial of the amount of data. (VERY INEFFICIENT AND SLOW)
        Ex. 5! = 5 * 4 * 3 * 2 * 1 = 120
            3! = 3 * 2 * 1 = 6
            1! = 1

    Big O tells you the "worst-case" scenario, like the longest it could possibly take.
    Big Omega tells you the "best-case" scenario, like the shortest it could possibly take.
    Big Theta tells you the "average-case" scenario, giving you a good idea of how it will usually perform. 

**AUGUST 18 2025**

Arrays & Dynamic Arrays
    - An array stores a collection of elements in contiguous which means elements are stored one after another in a single, unbroken block of mem.
    Ex of Contiguous Memory:
        - A row of houses on a street that are all built right next to each other.  If you know the address of the first house and you want to get to the 5th house, you can instantly calculate where it is. You don't have to visit houses 1 through 4 to find it.
    - Contiguous layout is the reason why accessing an element by its index is O(1) (Constant Time). The computer knows the starting address in memory and the size of each element, it can do a simple calculation (start_address + index * element_size) to jump to any element in one calculation.

    What happens when you want to insert an element at the beginning of an array?
        - Every element must shift one position to the right to make space for the new one.
        - This means the time complexity of insertion for an array is O(n) (Linear Time).
        - The amount of work required to insert an element grows in a direct, linear relationship with the number of items in the array.
    
    The Limit of a Fixed-Size Array
        - Fast O(1) reads, but slow O(n) insertions.
        - They are created with a fixed size.
    - What happens when you have an array size 10 and its full and you try to add an 11th element? (Overflow Error)

    The Dynamic Array (List)
        - An array that automatically grows itself when it runs out of space.
        - Under the hood, its just a regular array but with some extra space reserved at the end.
        - When you "append" an item and the array if full, Python performs a resize:
          - It creates a new, bigger array in memory (usually about double the size of the old one)
          - It copies all of the elements from the old, full array over to the new, bigger one.
          - It adds your new element at the end.
          - Finally, it deletes the old array
    - If there are n elements in the full array at the moment it needs to be resized, what is the Big O time complexity of that one specific "append" operation? (O(n))
    
    The Append Puzzle
        - Most of the time: append is fast and just placed the new item into one of the empty reserved slots (O(1))
        - Once in a while: append is very slow, as it triggers the O(n) resize and copy operation.
    - If someone asks for the Big O complexity of append, whats the correct answer? Is it O(1) or O(n)?

    Amortized Time
        - Since the O(n) resize happens so rarely compared to the O(1) operations, it becomes insignificant.
        - For this reason the complexity of a append on a dynamic array is described as amortized O(1).

    | Operation                  | Big O Notation     | Reasoning                                                   |
    | -------------------------- | :----------------: | ----------------------------------------------------------- |
    | Access (by index)          |        O(1)        | Direct memory calculation due to contiguous layout.         |
    | Search (by value)          |        O(n)        | Must check every element in the worst case.                 |
    | Insertion (at start/middle)|        O(n)        | Must shift all subsequent elements to make space.           |
    | Deletion (at start/middle) |        O(n)        | Must shift all subsequent elements to close the gap.        |
    | Append (add to end)        | `Amortized O(1)`   | Usually O(1), but occasionally O(n) when resizing is needed.|