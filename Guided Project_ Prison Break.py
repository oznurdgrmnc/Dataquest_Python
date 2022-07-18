/                                                                                                   0000777 0001750 0000000 00000000000 14252672661 007317  5                                                                                                    ustar                                                                   0000000 0000000                                                                                                                                                                        .ipynb_checkpoints/                                                                                 0000755 0001750 0000000 00000000000 14252341315 013012  5                                                                                                    ustar                                                                   0000000 0000000                                                                                                                                                                        .ipynb_checkpoints/Basics-checkpoint.ipynb                                                          0000777 0001750 0000000 00000001053 14252341315 017414  0                                                                                                    ustar                                                                   0000000 0000000                                                                                                                                                                        {
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Basics.ipynb                                                                                        0000777 0001750 0000000 00000241357 14252672661 011526  0                                                                                                    ustar                                                                   0000000 0000000                                                                                                                                                                        {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# My First Data Science Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Helicopter Escapes!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We begin by importing some helper functions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from helper import *"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "url = \"https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes\"\n",
    "data = data_from_url(url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's print the first three rows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['August 19, 1971', 'Santa Martha Acatitla', 'Mexico', 'Yes', 'Joel David Kaplan Carlos Antonio Contreras Castro', \"Joel David Kaplan was a New York businessman who had been arrested for murder in 1962 in Mexico City and was incarcerated at the Santa Martha Acatitla prison in the Iztapalapa borough of Mexico City. Joel's sister, Judy Kaplan, arranged the means to help Kaplan escape, and on August 19, 1971, a helicopter landed in the prison yard. The guards mistakenly thought this was an official visit. In two minutes, Kaplan and his cellmate Carlos Antonio Contreras, a Venezuelan counterfeiter, were able to board the craft and were piloted away, before any shots were fired.[9] Both men were flown to Texas and then different planes flew Kaplan to California and Castro to Guatemala.[3] The Mexican government never initiated extradition proceedings against Kaplan.[9] The escape is told in a book, The 10-Second Jailbreak: The Helicopter Escape of Joel David Kaplan.[4] It also inspired the 1975 action movie Breakout, which starred Charles Bronson and Robert Duvall.[9]\"]\n",
      "['October 31, 1973', 'Mountjoy Jail', 'Ireland', 'Yes', \"JB O'Hagan Seamus TwomeyKevin Mallon\", 'On October 31, 1973 an IRA member hijacked a helicopter and forced the pilot to land in the exercise yard of Dublin\\'s Mountjoy Jail\\'s D Wing at 3:40\\xa0p.m., October 31, 1973. Three members of the IRA were able to escape: JB O\\'Hagan, Seamus Twomey and Kevin Mallon. Another prisoner who also was in the prison was quoted as saying, \"One shamefaced screw apologised to the governor and said he thought it was the new Minister for Defence (Paddy Donegan) arriving. I told him it was our Minister of Defence leaving.\" The Mountjoy helicopter escape became Republican lore and was immortalized by \"The Helicopter Song\", which contains the lines \"It\\'s up like a bird and over the city. There\\'s three men a\\'missing I heard the warder say\".[1]']\n",
      "['May 24, 1978', 'United States Penitentiary, Marion', 'United States', 'No', 'Garrett Brock TrapnellMartin Joseph McNallyJames Kenneth Johnson', \"43-year-old Barbara Ann Oswald hijacked a Saint Louis-based charter helicopter and forced the pilot to land in the yard at USP Marion. While landing the aircraft, the pilot, Allen Barklage, who was a Vietnam War veteran, struggled with Oswald and managed to wrestle the gun away from her. Barklage then shot and killed Oswald, thwarting the escape.[10] A few months later Oswald's daughter hijacked TWA Flight 541 in an effort to free Trapnell.\"]\n"
     ]
    }
   ],
   "source": [
    "for i in data[:3]:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Removing the Details"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We initialize an index variable with the value of 0. The purpose of this variable is to help us track which row we're modifying."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "index = 0\n",
    "for i in data:\n",
    "    data[index] = i[:-1]\n",
    "    index += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['August 19, 1971', 'Santa Martha Acatitla', 'Mexico'], ['October 31, 1973', 'Mountjoy Jail', 'Ireland'], ['May 24, 1978', 'United States Penitentiary, Marion', 'United States']]\n"
     ]
    }
   ],
   "source": [
    "print(data[:3])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Extracting the Year"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the code cell below, we iterate over data using the iterable variable row and:\n",
    "\n",
    "* With every occurrence of `row[0]`, we refer to the first entry of `row`, i.e., the date.\n",
    "* Thus, with `date = fetch_year(row[0])`, we're extracting the year out of the date in `row[0]` and assigning it to the variable `date`.\n",
    "* We then replace the value of `row[0]` with the year that we just extracted."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "for row in data:\n",
    "    date = fetch_year(row[0]) \n",
    "    row[0] = date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1971, 'Santa Martha Acatitla', 'Mexico'], [1973, 'Mountjoy Jail', 'Ireland'], [1978, 'United States Penitentiary, Marion', 'United States']]\n"
     ]
    }
   ],
   "source": [
    "print(data[:3])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Attempts per Year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "min_year = min(data, key=lambda x: x[0])[0]\n",
    "max_year = max(data, key=lambda x: x[0])[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Before we move on, let's check what are the earliest and latest dates we have in our dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1971\n",
      "2020\n"
     ]
    }
   ],
   "source": [
    "print(min_year)\n",
    "print(max_year)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we'll create a list of all the years ranging from min_year to max_year. Our goal is to then determine how many prison break attempts there were for each year. Since years in which there weren't any prison breaks aren't present in the dataset, this will make sure we capture them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "years = []\n",
    "for y in range(min_year, max_year + 1):\n",
    "    years.append(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's take a look at years to see if it looks like we expected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]\n"
     ]
    }
   ],
   "source": [
    "print(years)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we create a list where each element looks like [<year>, 0]."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "attempts_per_year = []\n",
    "for y in years:\n",
    "    attempts_per_year.append([y, 0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And finally we increment the second entry (the one on index 1 which starts out as being 0) by 1 each time a year appears in the data.\n",
    "\n",
    "!!! IMPORTANT !!!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1971, 1], [1972, 0], [1973, 1], [1974, 0], [1975, 0], [1976, 0], [1977, 0], [1978, 1], [1979, 0], [1980, 0], [1981, 2], [1982, 0], [1983, 1], [1984, 0], [1985, 2], [1986, 3], [1987, 1], [1988, 1], [1989, 2], [1990, 1], [1991, 1], [1992, 2], [1993, 1], [1994, 0], [1995, 0], [1996, 1], [1997, 1], [1998, 0], [1999, 1], [2000, 2], [2001, 3], [2002, 2], [2003, 1], [2004, 0], [2005, 2], [2006, 1], [2007, 3], [2008, 0], [2009, 3], [2010, 1], [2011, 0], [2012, 1], [2013, 2], [2014, 1], [2015, 0], [2016, 1], [2017, 0], [2018, 1], [2019, 0], [2020, 1]]\n"
     ]
    }
   ],
   "source": [
    "for row in data:\n",
    "    for ya in attempts_per_year:\n",
    "        y = ya[0]\n",
    "        if row[0] == y:\n",
    "            ya[1] += 1\n",
    "            \n",
    "print(attempts_per_year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAvoAAASACAYAAACOdulIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD+naQAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdb1Sc5Z3/8Q8aBjH8W2iGiSKBHjUQsSFl2TKl0hgpbCRWhHRj7Zpgop7GgZQ/9Vhtm6Y9Kiaxf7RNdLcaSFcnsXRLUohG2ZBMNs2gZrZUSZpx05LQHjIjtmUUGmAS5vcgP6edTaoZSCDevF/n8GCu+3tf1/d+lI+311wTEQgEAgIAAABgKJdMdgMAAAAAzj+CPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAFNm+wGLqS0r+2Y7BaAKefoYyUfeH3v3r1av369XC6Xjh8/rubmZpWWlk5QdwAATB1hv9Gvr69Xbm6uYmNjZTabVVpaKrfbHVIzNDQkm82mpKQkxcTEqLy8XF6vN3j917/+tb74xS/qqquuUnR0tDIzM/XEE0+csdaePXv0yU9+UlFRUbr66qvV2NgY/hMCuKgMDg5q7ty52rBhw2S3AgCAoYUd9B0Oh2w2mzo6OtTW1ia/36+ioiINDg4Ga2pqatTS0qKmpiY5HA719vaqrKwseN3lcslsNuu5557TwYMH9fWvf10PPvigfvSjHwVruru7VVJSohtvvFGdnZ2qrq7W3XffrZdffnmcjwxgMi1cuFAPP/ywbrvttsluBQAAQ4sIBAKB8UzQ19cns9ksh8OhgoIC+Xw+zZgxQ3a7XYsXL5YkHT58WJmZmXI6ncrLyzvrPDabTb/5zW/U3t4uSXrggQe0Y8cOdXV1BWtuv/129ff3a+fOnefUG1t3gIn3YVt3/lZERARbdwAAuEDG/WVcn88nSUpMTJR0+m293+9XYWFhsCYjI0OpqalyOp0fOM/7c0iS0+kMmUOSiouLP3AOAAAAAKeN68u4o6Ojqq6uVn5+vrKysiRJHo9HJpNJCQkJIbXJycnyeDxnnWf//v164YUXtGPHX9/AezweJScnnzHHu+++qxMnTig6Ono8rQMAAACGNq6gb7PZ1NXVpX379o15jq6uLt1666361re+paKiovG0AwAAAOD/G/PWncrKSrW2tmr37t1KSUkJjlssFo2MjKi/vz+k3uv1ymKxhIwdOnRIN910k+6991594xvfCLlmsVhCTup5f464uDje5gMAAAAfIuygHwgEVFlZqebmZrW3tys9PT3kek5OjiIjI7Vr167gmNvtVk9Pj6xWa3Ds4MGDuvHGG7Vs2TI98sgjZ6xjtVpD5pCktra2kDkAfPQMDAyos7NTnZ2dkk6fsNXZ2amenp5J7gwAAGMJ+9Sd++67T3a7Xdu3b9fs2bOD4/Hx8cE37StXrtSLL76oxsZGxcXFqaqqStLpvfjS6e06CxYsUHFxsdavXx+c49JLL9WMGTMknf7HPysrSzabTcuXL1d7e7tWrVqlHTt2qLi4+Jx65dQdYOJ92Kk7e/bs0Y033njG+LJly/itDAAAzqOwg35ERMRZxxsaGlRRUSHp9A9m1dXVacuWLRoeHlZxcbE2btwY3LqzZs0affvb3z5jjlmzZuno0aPBz3v27FFNTY0OHTqklJQUffOb3wyuAQAAAODvG/c5+gAAAAAuPuM+Rx8AAADAxYegDwAAABgQQR8AAAAwIII+AAAAYEAEfQAAAMCACPoAAACAARH0AQAAAAMi6AMAAAAGRNAHAAAADIigDwAAABhQWEG/vr5eubm5io2NldlsVmlpqdxud0jN0NCQbDabkpKSFBMTo/Lycnm93pCaVatWKScnR1FRUcrOzj7rWj/96U+VnZ2tyy+/XLNmzdL69evDfDQAAABg6gor6DscDtlsNnV0dKitrU1+v19FRUUaHBwM1tTU1KilpUVNTU1yOBzq7e1VWVnZGXMtX75cS5YsOes6L730kr70pS/py1/+srq6urRx40Z9//vf149+9KMwHw8AAACYmiICgUBgrDf39fXJbDbL4XCooKBAPp9PM2bMkN1u1+LFiyVJhw8fVmZmppxOp/Ly8kLuX7NmjbZt26bOzs6Q8TvuuEN+v19NTU3BsR/+8Idat26denp6FBERMdaWAQAAgClhXHv0fT6fJCkxMVGS5HK55Pf7VVhYGKzJyMhQamqqnE7nOc87PDysyy67LGQsOjpaf/jDH3Ts2LHxtAwAAABMCWMO+qOjo6qurlZ+fr6ysrIkSR6PRyaTSQkJCSG1ycnJ8ng85zx3cXGxfv7zn2vXrl0aHR3VW2+9pe9+97uSpOPHj4+1ZQAAAGDKGHPQt9ls6urq0tatW89nP5Kke+65R5WVlVq0aJFMJpPy8vJ0++23S5IuuYSDggAAAIAPM6bUXFlZqdbWVu3evVspKSnBcYvFopGREfX394fUe71eWSyWc54/IiJCa9eu1cDAgI4dOyaPx6N/+qd/kiR9/OMfH0vLAAAAwJQSVtAPBAKqrKxUc3Oz2tvblZ6eHnI9JydHkZGR2rVrV3DM7Xarp6dHVqs17OYuvfRSXXnllTKZTNqyZYusVqtmzJgR9jwAAADAVDMtnGKbzSa73a7t27crNjY2uO8+Pj5e0dHRio+P14oVK1RbW6vExETFxcWpqqpKVqs15MSdI0eOaGBgQB6PRydOnAieujNnzhyZTCa98847+tnPfqb58+draGhIDQ0NweM6AQAAAHy4sI7X/HvHWjY0NKiiokLS6R/Mqqur05YtWzQ8PKzi4mJt3LgxZOvO/Pnzzxrau7u7lZaWpnfeeUe33HKL3nzzTQUCAVmtVj3yyCP61Kc+FebjAQAAAFPTuM7RBwAAAHBx4ggbAAAAwIAI+gAAAIABEfQBAAAAAyLoAwAAAAZE0AcAAAAMiKAPAAAAGBBBHwAAADAggj4AAABgQAR9ABNq7969uuWWW3TFFVcoIiJC27Ztm+yWAAAwpGmT3cCFlPa1HZPdAjDlHH2s5AOvDw4Oau7cuVq+fLnKysomqCsAAKaesN7o19fXKzc3V7GxsTKbzSotLZXb7Q6pGRoaks1mU1JSkmJiYlReXi6v1xtSs2rVKuXk5CgqKkrZ2dlnXevll19WXl6eYmNjNWPGDJWXl+vo0aPhPR2Ai87ChQv18MMP67bbbpvsVgAAMLSwgr7D4ZDNZlNHR4fa2trk9/tVVFSkwcHBYE1NTY1aWlrU1NQkh8Oh3t7es761W758uZYsWXLWdbq7u3XrrbdqwYIF6uzs1Msvv6x33nmHt38AAADAOQpr687OnTtDPjc2NspsNsvlcqmgoEA+n0/PPvus7Ha7FixYIElqaGhQZmamOjo6lJeXJ0l68sknJUl9fX164403zljH5XLp1KlTevjhh3XJJaf/W+SrX/2qbr31Vvn9fkVGRob/pAAAAMAUMq4v4/p8PklSYmKipNMB3e/3q7CwMFiTkZGh1NRUOZ3Oc543JydHl1xyiRoaGnTq1Cn5fD79x3/8hwoLCwn5AAAAwDkYc9AfHR1VdXW18vPzlZWVJUnyeDwymUxKSEgIqU1OTpbH4znnudPT0/XKK6/ooYceUlRUlBISEvSHP/xBP/3pT8faLgAAADCljDno22w2dXV1aevWreezH0mn/4Phnnvu0bJly/T666/L4XDIZDJp8eLFCgQC5309AAAAwGjGdLxmZWWlWltbtXfvXqWkpATHLRaLRkZG1N/fH/JW3+v1ymKxnPP8GzZsUHx8vNatWxcce+6553TVVVfp1VdfDe71B/DRMzAwoCNHjgQ/d3d3q7OzU4mJiUpNTZ3EzgAAMJaw3ugHAgFVVlaqublZ7e3tSk9PD7mek5OjyMhI7dq1KzjmdrvV09Mjq9V6zuv85S9/CX4J932XXnqppNNbhgB8dB04cEDz5s3TvHnzJEm1tbWaN2+eVq9ePcmdAQBgLGG90bfZbLLb7dq+fbtiY2OD++7j4+MVHR2t+Ph4rVixQrW1tUpMTFRcXJyqqqpktVpD3sIfOXJEAwMD8ng8OnHihDo7OyVJc+bMkclkUklJib7//e/rO9/5jr74xS/qvffe00MPPaRZs2YFwwGAj6b58+ezBQ8AgAkQEQjjX9yIiIizjjc0NKiiokLS6R/Mqqur05YtWzQ8PKzi4mJt3LgxZOvO/Pnz5XA4zpinu7tbaWlpkqStW7dq3bp1euutt3T55ZfLarVq7dq1ysjICOPxAAAAgKkprKAPAAAA4KNhXOfoAwAAALg4EfQBAAAAAyLoAwAAAAZE0AcAAAAMiKAPAAAAGBBBHwAAADAggj4AAABgQAR9AAAAwIAI+gAAAIABEfQBAAAAAwor6NfX1ys3N1exsbEym80qLS2V2+0OqRkaGpLNZlNSUpJiYmJUXl4ur9cbUrNq1Srl5OQoKipK2dnZZ6yzZs0aRUREnPE3ffr0MTwiAAAAMPWEFfQdDodsNps6OjrU1tYmv9+voqIiDQ4OBmtqamrU0tKipqYmORwO9fb2qqys7Iy5li9friVLlpx1na9+9as6fvx4yN+cOXP0hS98IczHAwAAAKamiEAgEBjrzX19fTKbzXI4HCooKJDP59OMGTNkt9u1ePFiSdLhw4eVmZkpp9OpvLy8kPvXrFmjbdu2qbOz8wPX+fWvf63s7Gzt3btXN9xww1jbBQAAAKaMce3R9/l8kqTExERJksvlkt/vV2FhYbAmIyNDqampcjqdY17nmWee0bXXXkvIBwAAAM7RmIP+6OioqqurlZ+fr6ysLEmSx+ORyWRSQkJCSG1ycrI8Hs+Y1hkaGtLzzz+vFStWjLVVAAAAYMqZNtYbbTaburq6tG/fvvPZzxmam5v13nvvadmyZRd0HQAAAMBIxvRGv7KyUq2trdq9e7dSUlKC4xaLRSMjI+rv7w+p93q9slgsY2rwmWee0aJFi5ScnDym+wEAAICpKKygHwgEVFlZqebmZrW3tys9PT3kek5OjiIjI7Vr167gmNvtVk9Pj6xWa9jNdXd3a/fu3WzbAQAAAMIU1tYdm80mu92u7du3KzY2NrjvPj4+XtHR0YqPj9eKFStUW1urxMRExcXFqaqqSlarNeTEnSNHjmhgYEAej0cnTpwInrozZ84cmUymYN2mTZs0c+ZMLVy48Hw8KwAAADBlhHW8ZkRExFnHGxoaVFFRIen0l2fr6uq0ZcsWDQ8Pq7i4WBs3bgzZujN//nw5HI4z5unu7lZaWpqk01/2nTVrlpYuXapHHnkkjEcCAAAAMK5z9AEAAABcnMZ1jj4AAACAixNBHwAAADAggj4AAABgQAR9AAAAwIAI+gAAAIABEfQBAAAAAyLoAwAAAAZE0AcAAAAMaNpkN3AhpX1tx2S3AEw5Rx8r+cDre/fu1fr16+VyuXT8+HE1NzertLR0groDAGDqCOuNfn19vXJzcxUbGyuz2azS0lK53e6QmqGhIdlsNiUlJSkmJkbl5eXyer0hNatWrVJOTo6ioqKUnZ191rUCgYAef/xxXXvttYqKitKVV16pRx55JMzHA3CxGRwc1Ny5c7Vhw4bJbgUAAEML642+w+GQzWZTbm6uTp48qYceekhFRUU6dOiQpk+fLkmqqanRjh071NTUpPj4eFVWVqqsrEy//OUvQ+Zavny5Xn31Vb3xxhtnXesrX/mKXnnlFT3++OO6/vrr9ac//Ul/+tOfxviYAC4WCxcu1MKFCye7DQAADC+soL9z586Qz42NjTKbzXK5XCooKJDP59Ozzz4ru92uBQsWSJIaGhqUmZmpjo4O5eXlSZKefPJJSVJfX99Zg/5vfvMbPfXUU+rq6tLs2bMlSenp6eE/HQAAADBFjevLuD6fT5KUmJgoSXK5XPL7/SosLAzWZGRkKDU1VU6n85znbWlp0cc//nG1trYqPT1daWlpuvvuu3mjDwAAAJyjMQf90dFRVVdXKz8/X1lZWZIkj8cjk8mkhISEkNrk5GR5PJ5znvt3v/udjh07pqamJv3kJz9RY2OjXC6XFi9ePNZ2AQAAgCllzKfu2Gw2dXV1ad++feezH0mn/yNieHhYP/nJT3TttddKkp599lnl5OTI7XYHt/MAAAAAOLsxvdGvrKxUa2urdu/erZSUlOC4xWLRyMiI+vv7Q+q9Xq8sFss5zz9z5kxNmzYtGPIlKTMzU5LU09MzlpYBAACAKSWsoB8IBFRZWanm5ma1t7ef8QXZnJwcRUZGateuXcExt9utnp4eWa3Wc14nPz9fJ0+e1G9/+9vg2FtvvSVJmjVrVjgtA7jIDAwMqLOzU52dnZKk7u5udXZ28h/xAACcZ2Ft3bHZbLLb7dq+fbtiY2OD++7j4+MVHR2t+Ph4rVixQrW1tUpMTFRcXJyqqqpktVqDJ+5I0pEjRzQwMCCPx6MTJ04E/8GfM2eOTCaTCgsL9clPflLLly/XD37wA42Ojspms+lzn/tcyFt+AB89Bw4c0I033hj8XFtbK0latmyZGhsbJ6krAACMJyIQCATOuTgi4qzjDQ0NqqiokHT6B7Pq6uq0ZcsWDQ8Pq7i4WBs3bgzZujN//nw5HI4z5unu7lZaWpokqbe3V1VVVXrllVc0ffp0LVy4UN/97neDJ/ycC34ZF5h4H/bLuAAAYGKEFfQBAAAAfDSM6xx9AAAAABcngj4AAABgQAR9AAAAwIAI+gAAAIABEfQBAAAAAyLoAwAAAAZE0AcAAAAMiKAPAAAAGBBBHwAAADAggj4AAABgQGEF/fr6euXm5io2NlZms1mlpaVyu90hNUNDQ7LZbEpKSlJMTIzKy8vl9XpDalatWqWcnBxFRUUpOzv7jHWOHj2qiIiIM/46OjrG8IgAAADA1BNW0Hc4HLLZbOro6FBbW5v8fr+Kioo0ODgYrKmpqVFLS4uamprkcDjU29ursrKyM+Zavny5lixZ8oHr/dd//ZeOHz8e/MvJyQmnXQAAAGDKiggEAoGx3tzX1yez2SyHw6GCggL5fD7NmDFDdrtdixcvliQdPnxYmZmZcjqdysvLC7l/zZo12rZtmzo7O0PGjx49qvT0dP3qV7866xt/AAAAAB9sXHv0fT6fJCkxMVGS5HK55Pf7VVhYGKzJyMhQamqqnE5n2PN//vOfl9ls1mc+8xn94he/GE+rAAAAwJQy5qA/Ojqq6upq5efnKysrS5Lk8XhkMpmUkJAQUpucnCyPx3POc8fExOi73/2umpqatGPHDn3mM59RaWkpYR8AAAA4R9PGeqPNZlNXV5f27dt3PvuRJH3sYx9TbW1t8HNubq56e3u1fv16ff7znz/v6wEAAABGM6Y3+pWVlWptbdXu3buVkpISHLdYLBoZGVF/f39IvdfrlcViGVejn/rUp3TkyJFxzQEAAABMFWEF/UAgoMrKSjU3N6u9vV3p6ekh13NychQZGaldu3YFx9xut3p6emS1WsfVaGdnp2bOnDmuOQAAAICpIqytOzabTXa7Xdu3b1dsbGxw3318fLyio6MVHx+vFStWqLa2VomJiYqLi1NVVZWsVmvIiTtHjhzRwMCAPB6PTpw4ETx1Z86cOTKZTNq8ebNMJpPmzZsnSfr5z3+uTZs26Zlnnjlfzw0AAAAYWljHa0ZERJx1vKGhQRUVFZJO/2BWXV2dtmzZouHhYRUXF2vjxo0hW3fmz58vh8Nxxjzd3d1KS0vT5s2btXbtWh07dkzTpk1TRkaG7r///uCRnQAAAAA+2LjO0QcAAABwcRrXOfoAAAAALk4EfQAAAMCACPoAAACAARH0AQAAAAMi6AMAAAAGRNAHAAAADIigDwAAABgQQR8AAAAwIII+gAm1d+9e3XLLLbriiisUERGhbdu2TXZLAAAY0rTJbuBCSvvajsluAZhyjj5W8oHXBwcHNXfuXC1fvlxlZWUT1BUAAFNPWG/06+vrlZubq9jYWJnNZpWWlsrtdofUDA0NyWazKSkpSTExMSovL5fX6w2pWbVqlXJychQVFaXs7OwPXPPIkSOKjY1VQkJCOK0CuEgtXLhQDz/8sG677bbJbgUAAEMLK+g7HA7ZbDZ1dHSora1Nfr9fRUVFGhwcDNbU1NSopaVFTU1Ncjgc6u3tPetbu+XLl2vJkiUfuJ7f79cXv/hF3XDDDeG0CQAAAEx5YW3d2blzZ8jnxsZGmc1muVwuFRQUyOfz6dlnn5XdbteCBQskSQ0NDcrMzFRHR4fy8vIkSU8++aQkqa+vT2+88cbfXe8b3/iGMjIydNNNN2n//v1hPRgAAAAwlY3ry7g+n0+SlJiYKElyuVzy+/0qLCwM1mRkZCg1NVVOpzOsudvb29XU1KQNGzaMp0UAAABgShrzl3FHR0dVXV2t/Px8ZWVlSZI8Ho9MJtMZ++mTk5Pl8XjOee4//vGPqqio0HPPPae4uLixtggAAABMWWMO+jabTV1dXdq3b9/57EeSdM899+iOO+5QQUHBeZ8bAAAAmArGtHWnsrJSra2t2r17t1JSUoLjFotFIyMj6u/vD6n3er2yWCznPH97e7sef/xxTZs2TdOmTdOKFSvk8/k0bdo0bdq0aSwtA7hIDAwMqLOzU52dnZKk7u5udXZ2qqenZ5I7AwDAWMJ6ox8IBFRVVaXm5mbt2bNH6enpIddzcnIUGRmpXbt2qby8XJLkdrvV09Mjq9V6zus4nU6dOnUq+Hn79u1au3at9u/fryuvvDKclgFcZA4cOKAbb7wx+Lm2tlaStGzZMjU2Nk5SVwAAGE9YQd9ms8lut2v79u2KjY0N7ruPj49XdHS04uPjtWLFCtXW1ioxMVFxcXGqqqqS1WoNnrgjnT4bf2BgQB6PRydOnAi+2ZszZ45MJpMyMzND1j1w4IAuueSS4HcBAHx0zZ8/X4FAYLLbAADA8CICYfyLGxERcdbxhoYGVVRUSDr9g1l1dXXasmWLhoeHVVxcrI0bN4Zs3Zk/f74cDscZ83R3dystLe2M8cbGRlVXV5+xJQgAAADA2YUV9AEAAAB8NIzrHH0AAAAAFyeCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAADq6+vV25urmJjY2U2m1VaWiq32z3ZbQGYAIb+Zdy0r+2Y7BYAALigjj5W8oHX//mf/1m33367cnNzdfLkST300EPq6urSoUOHNH369AnqEsBkCOuN/rm8FRgaGpLNZlNSUpJiYmJUXl4ur9cbUrNq1Srl5OQoKipK2dnZZ6zjdrt14403Kjk5WZdddpk+/vGP6xvf+Ib8fv8YHhEAgKlr586dqqio0HXXXae5c+eqsbFRPT09crlck90agAssrKDvcDhks9nU0dGhtrY2+f1+FRUVaXBwMFhTU1OjlpYWNTU1yeFwqLe3V2VlZWfMtXz5ci1ZsuSs60RGRmrp0qV65ZVX5Ha79YMf/EA//vGP9a1vfSvMxwMAAH/L5/NJkhITEye5EwAX2ri27vT19clsNsvhcKigoEA+n08zZsyQ3W7X4sWLJUmHDx9WZmamnE6n8vLyQu5fs2aNtm3bps7Ozg9dq7a2Vq+//rr++7//+5z7Y+sOAMDoPmzrzt8aHR3V5z//efX392vfvn0XsCsAF4NxfRn3/74VcLlc8vv9KiwsDNZkZGQoNTVVTqdzzOscOXJEO3fu1Gc/+9nxtAsAwJRms9nU1dWlrVu3TnYrACbAmIP+6OioqqurlZ+fr6ysLEmSx+ORyWRSQkJCSG1ycrI8Hk/Ya3z605/WZZddpmuuuUY33HCDvvOd74y1XQAAprTKykq1trZq9+7dSklJmex2AEyAMQf9iXgr8MILL+h//ud/ZLfbtWPHDj3++OMXbC0AAIwoEAiosrJSzc3Nam9vV3p6+mS3BGCCTBvLTe+/Fdi7d2/IWwGLxaKRkRH19/eHvNX3er2yWCxhr3PVVVdJkubMmaNTp07p3nvvVV1dnS699NKxtA0AwJRjs9lkt9u1fft2xcbGBv8Pe3x8vKKjoye5OwAXUlhv9D/srUBOTo4iIyO1a9eu4Jjb7VZPT4+sVuu4Gh0dHZXf79fo6Oi45gEAYCp56qmn5PP5NH/+fM2cOTP498ILL0x2awAusLDe6H/YW4H4+HitWLFCtbW1SkxMVFxcnKqqqmS1WkNO3Dly5IgGBgbk8Xh04sSJ4Kk7c+bMkclk0vPPP6/IyEhdf/31ioqK0oEDB/Tggw9qyZIlioyMPI+PDwCAsRn4dzEBfIiwjteMiIg463hDQ4MqKioknf7BrLq6Om3ZskXDw8MqLi7Wxo0bQ7buzJ8/Xw6H44x5uru7lZaWphdeeEHr1q3TW2+9pUAgoFmzZulf//VfVVNTo8suuyzMRwQAAACmnnGdow8AAADg4jSuc/QBAAAAXJwI+gAAAIABEfQBAAAAAyLoAwAAAAZE0AcAAAAMiKAPAAAAGBBBHwAAADAggj4AAABgQNMmu4ELKe1rOya7BWDKOfpYyQde37t3r9avXy+Xy6Xjx4+rublZpaWlE9QdAABTB2/0AUyowcFBzZ07Vxs2bG1ozkAAACAASURBVJjsVgAAMLSwgn59fb1yc3MVGxsrs9ms0tJSud3ukJqhoSHZbDYlJSUpJiZG5eXl8nq9ITWrVq1STk6OoqKilJ2dfcY6e/bs0a233qqZM2dq+vTpys7O1vPPPz+GxwNwsVm4cKEefvhh3XbbbZPdCgAAhhZW0Hc4HLLZbOro6FBbW5v8fr+Kioo0ODgYrKmpqVFLS4uamprkcDjU29ursrKyM+Zavny5lixZctZ19u/fr0984hP6z//8T73xxhu66667tHTpUrW2tob5eAAAAMDUFBEIBAJjvbmvr09ms1kOh0MFBQXy+XyaMWOG7Ha7Fi9eLEk6fPiwMjMz5XQ6lZeXF3L/mjVrtG3bNnV2dn7oWiUlJUpOTtamTZvOuT/26AMT78P26P+tiIgI9ugDAHCBjGuPvs/nkyQlJiZKklwul/x+vwoLC4M1GRkZSk1NldPpHM9S8vl8wXUAAAAAfLAxB/3R0VFVV1crPz9fWVlZkiSPxyOTyaSEhISQ2uTkZHk8njE3+dOf/lSvv/667rrrrjHPAQAAAEwlYz5e02azqaurS/v27Tuf/Zxh9+7duuuuu/TjH/9Y11133QVdCwAAADCKMQX9yspKtba2au/evUpJSQmOWywWjYyMqL+/P+StvtfrlcViCXsdh8OhW265Rd///ve1dOnSsbQK4CIzMDCgI0eOBD93d3ers7NTiYmJSk1NncTOAAAwlrC27gQCAVVWVqq5uVnt7e1KT08PuZ6Tk6PIyEjt2rUrOOZ2u9XT0yOr1RpWY3v27FFJSYnWrl2re++9N6x7AVy8Dhw4oHnz5mnevHmSpNraWs2bN0+rV6+e5M4AADCWsN7o22w22e12bd++XbGxscF99/Hx8YqOjlZ8fLxWrFih2tpaJSYmKi4uTlVVVbJarSEn7hw5ckQDAwPyeDw6ceJE8NSdOXPmyGQyaffu3Vq0aJG+8pWvqLy8PLiOyWTiC7nAR9z8+fM1jsO+AADAOQrreM2IiIizjjc0NKiiokLS6R/Mqqur05YtWzQ8PKzi4mJt3LgxZOvO/Pnz5XA4zpinu7tbaWlpqqio0ObNm8+4/tnPflZ79uw513YBAACAKWtc5+gDAAAAuDiN6xx9AAAAABcngj4AAABgQAR9AAAAwIAI+gAAAIABEfQBAAAAAyLoAwAAAAZE0AcAAAAMiKAPAAAAGBBBHwAAADCgsIJ+fX29cnNzFRsbK7PZrNLSUrnd7pCaoaEh2Ww2JSUlKSYmRuXl5fJ6vSE1q1atUk5OjqKiopSdnX3GOkNDQ6qoqND111+vadOmqbS0dAyPBgAAAExdYQV9h8Mhm82mjo4OtbW1ye/3q6ioSIODg8GampoatbS0qKmpSQ6HQ729vSorKztjruXLl2vJkiVnXefUqVOKjo7WqlWrVFhYGOYjAQAAAIgIBAKBsd7c19cns9ksh8OhgoIC+Xw+zZgxQ3a7XYsXL5YkHT58WJmZmXI6ncrLywu5f82aNdq2bZs6Ozv/7hoVFRXq7+/Xtm3bxtomAAAAMOWMa4++z+eTJCUmJkqSXC6X/H5/yFv4jIwMpaamyul0jmcpAAAAAGEYc9AfHR1VdXW18vPzlZWVJUnyeDwymUxKSEgIqU1OTpbH4xlfpwAAAADO2bSx3miz2dTV1aV9+/adz34AAAAAnAdjeqNfWVmp1tZW7d69WykpKcFxi8WikZER9ff3h9R7vV5ZLJbxdQoAAADgnIUV9AOBgCorK9Xc3Kz29nalp6eHXM/JyVFkZKR27doVHHO73erp6ZHVaj0/HQMAAAD4UGFt3bHZbLLb7dq+fbtiY2OD++7j4+MVHR2t+Ph4rVixQrW1tUpMTFRcXJyqqqpktVpDTtw5cuSIBgYG5PF4dOLEieCpO3PmzJHJZJIkHTp0SCMjI/rTn/6k9957L1hztnP3AQAAAIQK63jNiIiIs443NDSooqJC0ukfu6qrq9OWLVs0PDys4uJibdy4MWTrzvz58+VwOM6Yp7u7W2lpaZKktLQ0HTt27IyacZwGCgAAAEwZ4zpHHwAAAMDFaVzn6AMAAAC4OBH0AQAAAAMi6AMAAAAGRNAHAAAADIigDwAAABgQQR8AAAAwIII+AAAAYEAEfQAAAMCACPoAAACAAU2b7AYupLSv7ZjsFoAp5+hjJR94fe/evVq/fr1cLpeOHz+u5uZmlZaWTlB3AABMHWG90a+vr1dubq5iY2NlNptVWloqt9sdUjM0NCSbzaakpCTFxMSovLxcXq83pGbVqlXKyclRVFSUsrOzz7rWG2+8oRtuuEGXXXaZrrrqKq1bty7MRwNwMRocHNTcuXO1YcOGyW4FAABDCyvoOxwO2Ww2dXR0qK2tTX6/X0VFRRocHAzW1NTUqKWlRU1NTXI4HOrt7VVZWdkZcy1fvlxLliw56zrvvvuuioqKNGvWLLlcLq1fv15r1qzRv//7v4f5eAAuNgsXLtTDDz+s2267bbJbAQDA0MLaurNz586Qz42NjTKbzXK5XCooKJDP59Ozzz4ru92uBQsWSJIaGhqUmZmpjo4O5eXlSZKefPJJSVJfX5/eeOONM9Z5/vnnNTIyok2bNslkMum6665TZ2envve97+nee+8d04MCAAAAU8m4vozr8/kkSYmJiZIkl8slv9+vwsLCYE1GRoZSU1PldDrPeV6n06mCggKZTKbgWHFxsdxut/785z+Pp2UAAABgShhz0B8dHVV1dbXy8/OVlZUlSfJ4PDKZTEpISAipTU5OlsfjOee5PR6PkpOTz5jj/WsAAAAAPtiYT92x2Wzq6urSvn37zmc/AAAAAM6DMb3Rr6ysVGtrq3bv3q2UlJTguMVi0cjIiPr7+0PqvV6vLBbLOc9vsVjOOKnn/c/hzAMAAABMVWEF/UAgoMrKSjU3N6u9vV3p6ekh13NychQZGaldu3YFx9xut3p6emS1Ws95HavVqr1798rv9wfH2traNHv2bP3DP/xDOC0DuMgMDAyos7NTnZ2dkqTu7m51dnaqp6dnkjsDAMBYwgr6NptNzz33nOx2u2JjY+XxeOTxeHTixAlJUnx8vFasWKHa2lrt3r1bLpdLd911l6xWa/DEHUk6cuSIOjs7g/e+/4/+yMiIJOmOO+6QyWTSihUrdPDgQb3wwgt64oknVFtbex4fHcBkOHDggObNm6d58+ZJkmprazVv3jytXr16kjsDAMBYIgKBQOCciyMizjre0NCgiooKSad/MKuurk5btmzR8PCwiouLtXHjxpAtN/Pnz5fD4Thjnu7ubqWlpUk6/YNZNptNr7/+uj72sY+pqqpKDzzwQBiPBgAAAExdYQV9AAAAAB8N4zpHHwAAAMDFiaAPAAAAGBBBHwAAADAggj4AAABgQAR9AAAAwIAI+gAAAIABEfQBAAAAAyLoAwAAAAZE0AcAAADOo6eeekqf+MQnFBcXp7i4OFmtVr300ksT3oehfxk37Ws7JrsFAAAAGMzRx0o+8HpLS4suvfRSXXPNNQoEAtq8ebPWr1+vX/3qV7ruuusmqMsw3+jX19crNzdXsbGxMpvNKi0tldvtDqkZGhqSzWZTUlKSYmJiVF5eLq/XG1LT09OjkpISXX755TKbzbr//vt18uTJkJoNGzYoMzNT0dHRmj17tn7yk5+M8REBAACAiXPLLbfo5ptv1jXXXKNrr71WjzzyiGJiYtTR0TGhfYQV9B0Oh2w2mzo6OtTW1ia/36+ioiINDg4Ga2pqatTS0qKmpiY5HA719vaqrKwseP3UqVMqKSnRyMiI9u/fr82bN6uxsVGrV68O1jz11FN68MEHtWbNGh08eFDf/va3ZbPZ1NLSch4eGQAAAJgYp06d0tatWzU4OCir1Tqha49r605fX5/MZrMcDocKCgrk8/k0Y8YM2e12LV68WJJ0+PBhZWZmyul0Ki8vTy+99JIWLVqk3t5eJScnS5KefvppPfDAA+rr65PJZNKnP/1p5efna/369cG16urq9Oqrr2rfvn3n3B9bdwAAAHC+fdjWHUl68803ZbVaNTQ0pJiYGNntdt18880T0N1fjevLuD6fT5KUmJgoSXK5XPL7/SosLAzWZGRkKDU1VU6nU5LkdDp1/fXXB0O+JBUXF+vdd9/VwYMHJUnDw8O67LLLQtaKjo7Wa6+9Jr/fP56WAQAAgAtu9uzZ6uzs1KuvvqqVK1dq2bJlOnTo0IT2MOagPzo6qurqauXn5ysrK0uS5PF4ZDKZlJCQEFKbnJwsj8cTrPnbkP/+9fevSaeD/zPPPCOXy6VAIKADBw7omWeekd/v1zvvvDPWlgEAAIAJYTKZdPXVVysnJ0f19fWaO3eunnjiiQntYdpYb7TZbOrq6gprK825+uY3vymPx6O8vDwFAgElJydr2bJlWrdunS65hBNBAQAA8NEyOjqq4eHhCV1zTKm5srJSra2t2r17t1JSUoLjFotFIyMj6u/vD6n3er2yWCzBmv97Cs/7n9+viY6O1qZNm/SXv/xFR48eVU9Pj9LS0hQbG6sZM2aMpWUAAABgQjz44IPau3evjh49qjfffFMPPvig9uzZoy996UsT2kdYQT8QCKiyslLNzc1qb29Xenp6yPWcnBxFRkZq165dwTG3262enp7gt4ytVqvefPNNvf3228GatrY2xcXFac6cOSHzRUZGKiUlRZdeeqm2bt2qRYsW8UYfAAAAF7W3335bS5cu1ezZs3XTTTfp9ddf18svv6zPfe5zE9pHWKfu3HfffbLb7dq+fbtmz54dHI+Pj1d0dLQkaeXKlXrxxRfV2NiouLg4VVVVSZL2798v6fQRQ9nZ2briiiu0bt06eTwe3Xnnnbr77rv16KOPSpLeeustvfbaa/rUpz6lP//5z/re976ntrY2uVwupaWlnfPDceoOAAAAzrdzOXXnYhBW0I+IiDjreENDgyoqKiSd/sGsuro6bdmyRcPDwyouLtbGjRuD23Ik6dixY1q5cqX27Nmj6dOna9myZXrsscc0bdrprwz85je/0R133CG3263IyEjdeOONWrt2bch/XAAAAAD4+8Z1jj4AAACAixMb3gEAAAADIugDAAAABkTQBwAAAAyIoA8AAAAYEEEfAAAAMCCCPgAAAGBABH0AAADAgAj6AAAAgAER9AEAAAADIugDAAAABhRW0K+vr1dubq5iY2NlNptVWloqt9sdUjM0NCSbzaakpCTFxMSovLxcXq83pKanp0clJSW6/PLLZTabdf/99+vkyZMhNc8//7zmzp2ryy+/XDNnztTy5cv1xz/+cYyPCQAAAEwtYQV9h8Mhm82mjo4OtbW1ye/3q6ioSIODg8GampoatbS0qKmpSQ6HQ729vSorKwteP3XqlEpKSjQyMqL9+/dr8+bNamxs1OrVq4M1v/zlL7V06VKtWLFCBw8eVFNTk1577TXdc8895+GRAQAAAOOLCAQCgbHe3NfXJ7PZLIfDoYKCAvl8Ps2YMUN2u12LFy+WJB0+fFiZmZlyOp3Ky8vTSy+9pEWLFqm3t1fJycmSpKeffloPPPCA+vr6ZDKZ9Pjjj+upp57Sb3/72+BaP/zhD7V27Vr94Q9/GOcjAwAAAMY3rj36Pp9PkpSYmChJcrlc8vv9KiwsDNZkZGQoNTVVTqdTkuR0OnX99dcHQ74kFRcX691339XBgwclSVarVb///e/14osvKhAIyOv16mc/+5luvvnm8bQLAAAATBljDvqjo6Oqrq5Wfn6+srKyJEkej0cmk0kJCQkhtcnJyfJ4PMGavw35719//5ok5efn6/nnn9eSJUtkMplksVgUHx+vDRs2jLVdAAAAYEoZc9C32Wzq6urS1q1bz2c/kqRDhw7pK1/5ilavXi2Xy6WdO3fq6NGj+vKXv3ze1wIAAACMaNpYbqqsrFRra6v27t2rlJSU4LjFYtHIyIj6+/tD3up7vV5ZLJZgzWuvvRYy3/un8rxfU19fr/z8fN1///2SpE984hOaPn26brjhBj388MOaOXPmWNoGAAAApoyw3ugHAgFVVlaqublZ7e3tSk9PD7mek5OjyMhI7dq1KzjmdrvV09Mjq9Uq6fT++zfffFNvv/12sKatrU1xcXGaM2eOJOkvf/mLLrkktLVLL7002AMAAACADxbWqTv33Xef7Ha7tm/frtmzZwfH4+PjFR0dLUlauXKlXnzxRTU2NiouLk5VVVWSpP3790s6fbxmdna2rrjiCq1bt04ej0d33nmn7r77bj366KOSpMbGRt1zzz168sknVVxcrOPHj6u6ulqXXHKJXn311fP28AAAAIBRhRX0IyIizjre0NCgiooKSad/MKuurk5btmzR8PCwiouLtXHjxuC2HEk6duyYVq5cqT179mj69OlatmyZHnvsMU2b9tedRD/84Q/19NNPq7u7WwkJCVqwYIHWrl2rK6+8coyPCgAAAEwd4zpHHwAAAMDFaVzn6AMAAAC4OBH0AQAAAAMi6AMAAAAGRNAHAAAADIigDwAAABgQQR8AAAAwIII+AAAAYEAEfQAAAMCApn14yUdX2td2THYLAAAAMJijj5V84PWnnnpKTz31lI4ePSpJuu6667R69WotXLhwArr7K97oAwAAAOdRSkqKHnvsMblcLh04cEALFizQrbfeqoMHD05oH2EH/fr6euXm5io2NlZms1mlpaVyu90hNUNDQ7LZbEpKSlJMTIzKy8vl9XpDanp6elRSUqLLL79cZrNZ999/v06ePBm8XlFRoYiIiDP+rrvuujE+KgAAAHDh3XLLLbr55pt1zTXX6Nprr9UjjzyimJgYdXR0TGgfYQd9h8Mhm82mjo4OtbW1ye/3q6ioSIODg8GampoatbS0qKmpSQ6HQ729vSorKwte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5ZVXXrnLaYrIvSI5OZmXXnqJOXPmDHQrIiIiXq3bQb+kpASbzcbRo0cpLCykvb0dq9WK0+n01GRlZbF//37y8/MpKSnhwoULXVbubt68SUpKCi6XiyNHjrBr1y5yc3N54YUXPDUhISFkZmZSWlrK//7v/7J+/XrWr1/Pj3/84x5OWURERETE+xncbre7Jxe4dOkSkZGRlJSU8MQTT9DS0oLJZCIvL4/58+cDcPLkScaNG0dFRQUJCQm8+eabzJo1iwsXLjBixAgAdu7cyZo1a7h06RL+/v53vNfcuXMJCQnhZz/72afqTVt3RPrfJ23d+TCDwcDevXtJS0vrw45EREQGpx5/GbelpQWAiIgIAI4fP057eztJSUmemtjYWCwWCxUVFQBUVFTw8MMPe0I+wIwZM3jvvfc4ceLEHe9TWVnJkSNH+PznP9/TlkVEREREvF6Pvozb0dHBypUrmTp1Kg899BAATU1N+Pv7Ex4e3qV2xIgRNDU1eWo+HPI7xzvHPmzkyJFcunSJGzdu8O1vf5slS5b0pGURERERkUGhR0HfZrNRU1NDWVlZb/Vzm9/+9re0trZy9OhR1q5dy/33388///M/99n9RERERES8wV0H/czMTA4cOEBpaSkjR470PG82m3G5XDQ3N3dZ1Xc4HJjNZk/N7373uy7X6zyVp7Om05gxYwB4+OGHcTgcfPvb31bQF/kb1trayunTpz2Pz549S1VVFREREVgslgHsTERExLt0e4++2+0mMzOTvXv3YrfbPUG8U3x8PH5+frz99tue52pra2loaCAxMRGAxMREqquruXjxoqemsLAQo9HI+PHj/+q9Ozo6aGtr627LInIPOXbsGI899hiPPfYYANnZ2Tz22GNdTt0SERGRnuv2ir7NZiMvL4+CggKGDBni2VMfFhZGUFAQYWFhLF68mOzsbCIiIjAajSxfvpzExEQSEhIAsFqtjB8/noULF7JlyxaamppYv349NpuNgIAAALZt24bFYiE2Nha49d80v/e97/H1r3+9t+YuIgNg2rRp9PCwLxEREfkUun28psFguOPzOTk5ZGRkALf+YdZzzz3H7t27aWtrY8aMGWzfvr3Ltpx3332XZcuWUVxcTEhICOnp6WzatAlf31ufPV577TVef/11zp49i6+vL/fddx9f+cpX+OpXv4qPT48PCxIRERER8Wo9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VVVVvPPOOyxbtoz09HT+9Kc/9WsPd33qjs1mo6amhrKyst7sR0RERETkb56/vz/3338/APHx8fz+97/nRz/6Ea+//nq/9XBXK/qZmZkcOHCAoqIiRo4c6XnebDbjcrlobm7uUu9wODCbzZ6aj57C0/m4s0ZERERExJt0dHTQ1tbWr/fsVtB3u91kZmayd+9e7HY7Y8aM6TIeHx+Pn58fb7/9tue52tpaGhoaSExMBCAxMZHq6mouXrzoqSksLMRoNPb7viURERERkd62bt06SktLOXfuHNXV1axbt47i4mK+9KUv9Wsf3dq6Y7PZyMvLo6CggCFDhnj21IeFhREUFERYWBiLFy8mOzubiIgIjEYjy5cvJzExkYSEBACsVivjx49n4cKFbNmyhaamJtavX4/NZiMgIMBzr6qqKgBaW1u5dOkSVVVV+Pv768OAiIiIiNzTLl68yKJFi2hsbCQsLIxHHnmEt956i6eeeqpf++jW8ZoGg+GOz+fk5JCRkQHc+odZzz33HLt376atrY0ZM2awffv2Ltty3n33XZYtW0ZxcTEhISGkp6ezadMmfH0/+Nxxp3uNGjXK8x/GPg0drykiIiIiva07x2sOpB6doy8iIiIiIvemHp2jLyIiIiIi9yYFfRERERERL6SgLyIiIiLihRT0RURERES8kIK+iIiIiIgXUtAXEREREfFCCvoiIiIiIl5IQV9ERERExAsp6IuIiIiIeCHfgW6gL41ee3CgWxAREelT5zalfOz4xo0b2bNnDydPniQoKIgpU6awefNmYmJi+qlDERko3V7R37hxI48//jhDhgwhMjKStLQ0amtru9Rcv34dm83GsGHDCA0NZd68eTgcji41DQ0NpKSkEBwcTGRkJKtXr+bGjRtdaoqLi5k4cSIBAQHcf//95Obmdn+GIiIig1hJSQk2m42jR49SWFhIe3s7VqsVp9M50K2JSB/rdtD/NG8YWVlZ7N+/n/z8fEpKSrhw4QJz5871jN+8eZOUlBRcLhdHjhxh165d5Obm8sILL3hqzp49S0pKCtOnT6eqqoqVK1eyZMkS3nrrrR5OWUREZPA4dOgQGRkZxMXFMWHCBHJzc2loaOD48eMD3ZqI9DGD2+129+QCly5dIjIykpKSEp544glaWlowmUzk5eUxf/58AE6ePMm4ceOoqKggISGBN998k1mzZnHh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bu4AdSUiIuJ9uh30P2k1Lj8/H5PJhMViobq6mhUrVpCWlobVavW8Jicnh3HjxmEymaioqGDFihVkZWURExPT5V52u52zZ8+yZMmSHkxRRO4l06ZNw+12D3QbIiIiXs/g7uZv3OLi4i6rcZ06V+NeffVVtm7disPhICoqikWLFrFhwwb8/f09tWvXriU3N5crV64wevRoli5dSlZW1m1HZz7zzDO8++67lJeX3+X0REREREQGp24HfRERERERuff16qk7IiIiIiJyb1DQFxERERHxQgr6IiIiIiJeSEFfRERERMQLKeiLiIiIiHghBX0RERERES+koC8iIiIi4oUU9EVEREREvJDvQDfQl0avPTjQLYgMOuc2pXzseGlpKVu3buX48eM0Njayd+9e0tLS+qk7ERGRwaPbK/qlpaWkpqYSHR2NwWBg3759XcYdDgcZGRlER0cTHBzMzJkzqaur61JTX1/PnDlzMJlMGI1GFixYgMPhuO1eBw8eZPLkyQQFBTF06FCFAREv4HQ6mTBhAtu2bRvoVkRERLxat4P+x/2SdrvdpKWlcebMGQoKCqisrGTUqFEkJSXhdDo9r7darRgMBux2O+Xl5bhcLlJTU+no6PBc69e//jULFy7ky1/+Mn/84x8pLy/nmWee6cFUReRekJyczEsvvcScOXMGuhURERGv1u2tO8nJySQnJ99xrK6ujqNHj1JTU0NcXBwAO3bswGw2s3v3bpYsWUJ5eTnnzp2jsrISo9EIwK5duxg6dCh2u52kpCRu3LjBihUr2Lp1K4sXL/Zcf/z48XczRxERERGRQadXv4zb1tYGQGBg4Ac38PEhICCAsrIyT43BYCAgIMBTExgYiI+Pj6fmD3/4A3/+85/x8fHhscceIyoqiuTkZGpqanqzXRERERERr9WrQT82NhaLxcK6deu4evUqLpeLzZs3c/78eRobGwFISEggJCSENWvWcO3aNZxOJ6tWreLmzZuemjNnzgDw7W9/m/Xr13PgwAGGDh3KtGnTuHLlSm+2LCIiIiLilXo16Pv5+bFnzx5OnTpFREQEwcHBFBUVkZycjI/PrVuZTCby8/PZv38/oaGhhIWF0dzczMSJEz01nXv1n3/+eebNm0d8fDw5OTkYDAby8/N7s2UREREREa/U68drxsfHU1VVRUtLCy6XC5PJxOTJk5k0aZKnxmq1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S3nkkUcCf6Xvg5CfkJDA9u3b+d3vfhf4rNlsvp79ioiIzCnX8XI9EfkzN+3Xax47dozMzMwr7hcWFlJXV8eOHTuorq5maGiI+Ph4CgoKqKysZMGCBYHa8vJy6urqGB4eZvny5Tz00EM88sgjGAwGAOrq6rj//vuvur7+wRIRERER+WjX9R59ERERERG5Oengu4iIiIhICFLQFxEREREJQQr6IiIiIiIhSEFfRERERCQEKeiLiIiIiIQgBX0RERERkRCkoC8iIiIiEoIU9EVEREREQtD82W5gJi0vf2G2WxCZc85su/tDx9vb26murqazs5OBgQEaGxtxOBw3qDsREZG5Y9pP9Nvb28nNzcVisWAwGGhqapoyPjQ0RFFRERaLhaioKHJycvB4PFNq+vr6WL9+PSaTicWLF5OXl8fQ0NCUmieffJL09HSioqJYsmTJNWxNRG5G4+PjJCcnU1NTM9utiIiIhLRpB/0P+yXt9/txOBycOnWK5uZmurq6SEhIICsri/Hx8cDns7OzMRgMHD16lJdeegmv10tubi4+ny8wl9fr5d577+Wb3/zmdWxPRG42drudJ554gvXr1892KyIiIiFt2kd37HY7drv9qmMej4cTJ07Q3d1NUlISALW1tZjNZvbu3UtxcTEvvfQSZ86coauri8WLFwOwZ88eli5dytGjR8nKygLg8ccfB6Curu5a9iUiIiIiMqcF9cu4ExMTAERGRl5eICyMiIgIOjo6AjUGg4GIiIhATWRkJGFhYYEaERERERG5PkEN+itXrsRqtVJRUcG5c+fwer1UVVXR39/PwMAAAJ/73OeIjo7m0Ucf5fz584yPj7Nlyxbef//9QI2IiIiIiFyfoAb98PBwGhoa6OnpwWg0EhUVRVtbG3a7nbCwS0uZTCbq6+t5/vnniYmJITY2lpGREVavXh2oERERERGR6xP012umpqbicrkYHR3F6/ViMplIS0tjzZo1gZrs7Gz6+vp49913mT9/PkuWLMFsNnP77bcHux0RERERkTlpxt6jHxsbC1z6gq7T6eSHP/zhFTXLli0D4OjRo7zzzjvcc889M9WOiNwkxsbG6O3tDVyfPn0al8uF0WjEarXOYmciIiKhZdpB/6N+SdfX12MymbBarbjdbkpLS3E4HGRnZwc+s3v3blatWoXJZOKVV16htLSURx55hMTExEDN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BJ/5zGcwGAy4XK7ptisiIiIiMidNO+iPj4+TnJxMTU3NFWN+vx+Hw8GpU6dobm6mq6uLhIQEsrKyGB8fD9QVFBRw8uRJDh06hNvtZsOGDeTl5dHV1XXFnP/wD/+AxWKZbpsiIiIiInOawe/3+6/5wwYDjY2NOBwOAHp6ekhMTKS7u5ukpCQAfD4fZrOZp556iuLiYgBiYmKora0lPz8/MFdcXBxVVVWBGoCf//znlJWVcfDgQZKSkujq6uIzn/nMtbYrIiIiIjJnBPWM/sTEBACRkZGXFwgLIyIigo6OjsC99PR09u/fz/DwMD6fj3379nHhwgUyMjICNUNDQzz44IP8+7//O1FRUcFsU0REREQk5AU16K9cuRKr1UpFRQXnzp3D6/VSVVVFf38/AwMDgboDBw4wOTlJXFwcERERlJSU0NjYiM1mAy4dASoqKuKhhx5izZo1wWxRRERERGROCGrQDw8Pp6GhgZ6eHoxGI1FRUbS1tWG32wkLu7xUZWUlIyMjHDlyBKfTSVlZGXl5ebjdbgB+/OMf87//+79UVFQEsz0RERERkTkjqGf0/9Do6CherxeTyURaWhpr1qyhpqaGvr4+bDbblHP8AFlZWdhsNnbt2oXD4eD555/HYDAExt9//33mzZvHfffdx549e661ZRERERGROWH+TE0cGxsLgMfjwel08sMf/hCA8+fPA0x5wg8wb948fD4fADt27OCJJ54IjL399tvcdddd7N+/n7S0tJlqWUREREQkZEw76I+NjdHb2xu4Pn36NC6XC6PRiNVqpb6+HpPJhNVqxe12U1paisPhIDs7G7h0jt9ms1FSUsL27duJi4ujqamJ1tZWWlpaALBarVPWjImJAeDjH/84t9566zVvVkRERERkrph20Hc6nWRmZgauy8rKACgsLKSuro6BgQHKysoYGhoiPj6egoICKisrA/Xh4eG8+OKLlJeXk5uby9jYGDabjT179rB27dogbElERERERK7rjL6IiIiIiNycgvrWHRERERERuTko6IuIiIiIhCAFfRERERGREKSgLyIiIiISghT0RURERERCkIK+iIiIiEgIUtAXEREREQlBCvoiIiIiIiFIQV9Ebqj29nZyc3OxWCwYDAaamppmuyUREZGQNH+2G5hJy8tfmO0WROacM9vu/tDx8fFxkpOTeeCBB9iwYcMN6kpE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\n",
      "text/plain": [
       "<Figure size 900x1500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "barplot(attempts_per_year)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The years in which the most helicopter prison break attempts occurred were 1986, 2001, 2007 and 2009, with a total of three attempts each."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Attempts by Country"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Country</th>\n",
       "      <th>Number of Occurrences</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>France</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>United States</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Greece</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Belgium</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Canada</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Brazil</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>United Kingdom</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Australia</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Chile</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Puerto Rico</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Italy</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Netherlands</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Ireland</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Mexico</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Russia</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "countries_frequency = df[\"Country\"].value_counts()\n",
    "print_pretty_table(countries_frequency)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By and far, the country with the most helicopter prison escape attempts is France."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
                                                                                                                                                                                                                                                                                 helper.py                                                                                           0000777 0001750 0000000 00000003553 00000000000 011030  0                                                                                                    ustar                                                                   0000000 0000000                                                                                                                                                                        import pandas as pd
import re
import matplotlib.pyplot as plt
from IPython.core.display import display, HTML

def data_from_url(url):
    df = pd.read_html(url)[1]
    lol = df.to_numpy().tolist()
    return lol

def fetch_year(date_string):
    return int(re.findall("\d{4}", date_string)[0])

def barplot(list_of_2_element_list):
    d = {ya[0]:ya[1] for ya in list_of_2_element_list}
    plt.figure(figsize=(9,15))
    axes = plt.axes()
    axes.get_xaxis().set_visible(False)

    spines = axes.spines
    spines['top'].set_visible(False)
    spines['right'].set_visible(False)
    spines['bottom'].set_visible(False)
    spines['left'].set_visible(False)
    ax = plt.barh(*zip(*d.items()), height=.5)
    plt.yticks(list(d.keys()), list(d.keys()))
    plt.xticks(range(4), range(4))
    rectangles = ax.patches
    for rectangle in rectangles:
        x_value = rectangle.get_width()
        y_value = rectangle.get_y() + rectangle.get_height() / 2
        space = 5
        ha = 'left'
        label = "{}".format(x_value)
        if x_value > 0:
            plt.annotate(
                label,
                (x_value, y_value),
                xytext=(space, 0),
                textcoords="offset points",
                va='center',
                ha=ha)

    axes.tick_params(tick1On=False)
    plt.show()

def unique_countries(countries):
    s = pd.Series(countries)
    return list(s.unique())

def display_no_index(df):
    display(HTML(df.to_html(index=False)))
    
def print_pretty_table(countries_frequency):
    countries = df.Country.value_counts().index
    occurrences = df.Country.value_counts().values
    d = {"Country": countries, "Number of Occurrences": occurrences}
    display_no_index(pd.DataFrame(d))

df = pd.read_html("https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes")[1]
df = df[["Date", "Prison name", "Country", "Succeeded", "Escapee(s)"]]
                                                                                                                                                     