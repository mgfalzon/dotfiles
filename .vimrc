set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" My Plugins
Plugin 'jreybert/vimagit'
Plugin 'preservim/nerdtree'
Plugin 'vifm/vifm.vim'
Plugin 'mattn/emmet-vim'
Plugin 'tpope/vim-surround'     
Plugin 'sheerun/vim-polyglot'
Plugin 'chriskempson/base16-vim'
Plugin 'ap/vim-css-color'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" Plugin Settings
map <C-b> :NERDTreeToggle<CR>
map <Leader>vv :Vifm<CR>

"Basic Settings"
set nocompatible
inoremap jj <Esc>
syntax on
set number
set hidden
set mouse=a
set smartindent
set clipboard=unnamed

"Spacing"
set expandtab
set ts=4 sw=4

"Splits"
set splitbelow splitright
inoremap <C-h> <C-w>h
inoremap <C-j> <C-w>j
inoremap <C-k> <C-k>k
inoremap <C-l> <C-l>l

if filereadable(expand("~/.vimrc_background"))
  let base16colorspace=256
  source ~/.vimrc_background
endif
