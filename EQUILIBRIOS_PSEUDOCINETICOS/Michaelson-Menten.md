# Modelo cinético de Michaelson-Menden

Se modela la velocidad de una reacción catalizada por enzimas. Es de uso común en biología pues se usa para describir la absorción de nutrientes por parte de células cultivadas. 

$$
E+S\overset{k_f,k_r}{\longleftrightarrow}\left[ES\right]\overset{k_c}{\longleftrightarrow} E+P
$$

La enzima $E$ interactua con el sustrato $S$ para formar un complejo $[ES]$. Posteriormente, este complejo se descompone, consumiendo el sustrato, regenerando la enzima y produciendo un producto $P$. $k_f,k_r$ son las constantes de velocidad de asociación y disociación ezima-sustrato respectivamente; $k_c$ es la constante de velocidad de disociación del complejo para la formación del producto.

## Aproximación de rápido equilibrio

La velocidad de formación de producto varía linealmente con la concentración de complejo

$$
\frac{\partial [P]}{\partial t} = k_c[ES]
$$

La condición de rápido equilibrio implica que en el estado inicial, la concentración velocidad

$$
\begin{align*}
k_f\left[E\right]\left[S\right]=k_r\left[ES\right] + k_c\left[ES\right]\longrightarrow \frac{\left[E\right]\left[S\right]}{\left[ES\right]}=\frac{k_c+k_r}{k_f}
\end{align*}
$$



## Aproximación de estado estable

La velocidad de formación de producto varía linealmente con la concentración de complejo

$$
\frac{\partial [P]}{\partial t} = k_c[ES]
$$

La condición de estado estable implica que en el estado inicial, la formación y disociación de complejo suceden a la misma velocidad

$$
k_f\left[E\right]\left[S\right]=k_r\left[ES\right] + k_c\left[ES\right]\longrightarrow\left[E\right]\left[S\right]=\frac{k_c+k_r}{k_f} \left[ES\right]
$$


