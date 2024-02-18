# This file is authored by Peter Urban, Ghent University, and is subject to the MPL-2.0 license.
# SPDX-License-Identifier: MPL-2.0

import os
from pathlib import Path
import pickle
from collections import defaultdict
from typing import List, Dict, Union

def get_cache_file_name(
    folder_path: Union[str, Path], 
    cache_root: Union[str, Path, None] = None, 
    cache_name: str = 'tmtgp.index', 
    create_dir: bool = True) -> Path:
    """Return the path to the cache file for a given folder path

    Parameters
    ----------
    folder_path : str or Path
        The path to the folder containing files that are indexed
    cache_root : str or Path, optional
        The path to the root folder containing all cache files. If None, the cache file will be in the same folder as the data files
    cache_name : str, optional
        The name of the cache file
    create_dir : bool, optional
        If true: create a subdirectory, by default True

    Returns
    -------
    Path
        The path to the cache file
    """
    
    if cache_root is None:
        return Path(folder_path) / Path(cache_name)
            
    cache_file = Path(os.path.abspath(cache_root))
    folder_path = Path(os.path.abspath(folder_path))
    root_path = 'root_' + folder_path.parts[0]
    root_path = root_path.replace(':', '')

    cache_file = cache_file.joinpath(root_path, *folder_path.parts[1:], cache_name)
    
    if create_dir:
        os.makedirs(cache_file.parent, exist_ok=True)
    
    return cache_file


def load_index_cache_files(
    file_paths: List[str], 
    force_new: bool = False, 
    cache_name: str = 'tmtgp.index', 
    cache_root: str = 'cache', 
    update_cache: Dict[str, str] = None, 
    verbose: bool = False, 
    create_dir: bool = True) -> Dict[str, str]:
    """Load index files for a given list of file paths

    Parameters
    ----------
    file_paths : list of str
        The list of file paths to load index files for
    force_new : bool, optional
        If true: force the creation of new cache files, by default False
    cache_name : str, optional
        The name of the cache file, by default 'tmtgp.index'
    cache_root : str, optional
        The path to the root folder containing all cache files, by default 'cache'
    update_cache : dict, optional
        A dictionary to update with the loaded cache data, by default None
    verbose : bool, optional
        If true: print verbose output, by default False
    create_dir : bool, optional
        If true: create a subdirectory, by default True

    Returns
    -------
    dict
        A dictionary containing the loaded index cache data
    """
    
    if update_cache is None:
        cache = {}
    else:
        cache = update_cache
        
    loaded_index_cache_files = set()
    
    # look for existing files in each folder
    for fp in file_paths:
        try:
            folder_path, file = os.path.split(fp)
            
            index_file = get_cache_file_name(folder_path, cache_root, cache_name, create_dir=create_dir)            
            
            if index_file in loaded_index_cache_files:
                continue
                
            loaded_index_cache_files.add(index_file)
            
            if os.path.exists(index_file) and not force_new:
                if verbose:
                    print('Open:', index_file)
                load_index = pickle.load(open(index_file, 'rb'))
                cache.update(load_index)
        except:
            pass
            
    return cache


def update_index_cache_files(cached_index_dict: Dict[str, str], force_new: bool = False, cache_name: str = 'tmtgp.index', cache_root: str = 'cache', verbose: bool = False, create_dir: bool = True) -> None:
    """Update index cache files with a given dictionary of index data

    Parameters
    ----------
    cached_index_dict : dict
        A dictionary containing the index data to update the index files with
    force_new : bool, optional
        If true: force the creation of new index files, by default False
    cache_name : str, optional
        The name of the index file, by default 'tmtgp.index'
    cache_root : str, optional
        The path to the root folder containing all cache files, by default 'cache'
    verbose : bool, optional
        If true: print verbose output, by default False
    create_dir : bool, optional
        If true: create a subdirectory, by default True
    """
    
    # group cache dict into per folder cache files
    cache_per_folder = defaultdict(dict)
    for k, v in cached_index_dict.items():
        folder_path, file = os.path.split(k)        
        index_file = get_cache_file_name(folder_path, cache_root, cache_name, create_dir=create_dir)    
        cache_per_folder[index_file].update({k: v})
        
    # write an cache file into each folder
    for index_file, index in cache_per_folder.items():
        if verbose:
            print(index_file)
        
        if not os.path.exists(index_file) or force_new:
            write_cache = {}
        else:
            try:
                write_cache = pickle.load(open(index_file, 'rb'))
            except:
                write_cache = {}
            
        write_cache.update(index)
        pickle.dump(write_cache, open(index_file, 'wb'))