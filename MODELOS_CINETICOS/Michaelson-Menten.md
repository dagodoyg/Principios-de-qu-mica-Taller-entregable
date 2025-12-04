# ****1\. Modelo cinético de Michaelson-Menten****

Se modela la velocidad de una reacción catalizada por enzimas. Es de uso común en biología pues se usa para describir la absorción de nutrientes por parte de células cultivadas. 

$$
E+S\overset{k_f,k_r}{\longleftrightarrow}\left[ES\right]\overset{k_c}{\longleftrightarrow} E+P
$$

La enzima $E$ interactua con el sustrato $S$ para formar un complejo $[ES]$. Posteriormente, este complejo se descompone, consumiendo el sustrato, regenerando la enzima y produciendo un producto $P$. $k_f,k_r$ son las constantes de velocidad de asociación y disociación ezima-sustrato respectivamente; $k_c$ es la constante de velocidad de disociación del complejo para la formación del producto.

## ****Aproximación de rápido equilibrio****

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



## ****Aproximación de estado estático****

La velocidad de formación de producto varía linealmente con la concentración de complejo

$$
\begin{align}
\frac{\partial [P]}{\partial t} = k_c[ES] \quad (1)
\end{align}
$$

La condición de estado estable implica que en el estado inicial, la formación y disociación de complejo suceden a la misma velocidad

$$
k_f\left[E\right]\left[S\right]=k_r\left[ES\right] + k_c\left[ES\right]\longrightarrow\left[E\right]\left[S\right]=\frac{k_c+k_r}{k_f} \left[ES\right]=k_m\left[ES\right]
$$

$k_m$ es la constante de Michaelis-Menten. Un $k_m$ bajo indica una velocidad de formación de complejo mayor a la de disociación, es decir, que la enzima de enlaza fuertemente al sustrato. Por otro lado, un $k_m$ alto se da cuando la velocidad de disociación de complejo es mayor a la de formación, evidenciando una baja afinidad de la enzima por el sustrato, pues se enlaza débilmente.

La concentración total de enzima en el sistema es la suma de las concentraciones de enzima libre $\left[E\right]$ y enzima fijada en los sitios activos al sustrato $\left[ES\right]$, es decir, $\left[E\right]_T=\left[E\right]+\left[ES\right]$. De donde $\left[E\right]=\left[E\right]_T-\left[ES\right]$. Así

$$
\left(\left[E\right]_T-\left[ES\right]\right)\left[S\right]=k_m\left[ES\right]\longrightarrow \left[ES\right]=\frac{\left[E\right]_T \left[S\right]}{k_m+\left[S\right]}
$$

Sustituyendo en la ecuación (1) 

$$
\frac{\partial P}{\partial t} = k_c\frac{[E]_T[S]}{k_m + [S]}
$$

Si la concentración de sustrato $[S]$ es mucho mayor a $k_m$, entonces \frac{\partial P}{\partial t}_{[S]\gg k_m} = k_c[E]_T = V_{max}, es la velocidad máxima de la reacción, puesto que en este estado casi toda la enzima se encuentra ligada a los sitios activos del sustrato y la velocidad de formación de producto ya no depende de la concentración de sustrato. Así

$$
\frac{\partial P}{\partial t} = \frac{V_max[S]}{k_m + [S]}
$$

Es la ecuación de Michaelis-Menten. Nótese que si $[S]=k_m$, entonces  $\frac{\partial P}{\partial t} = \frac{V_max}{2}$, luego $k_m$ es la concentración necesaria de sustrato para que la velocidad de reacción sea la mitad de la máxima posible, que sucede cuando aproximadamente la mitad del sustrato se encuentran ligados a la enzima. Finalmente, si $[S]\ll k_m$, entonces $\frac{\partial P}{\partial t} = \frac{V_max[S]}{k_m}$, la velocidad de la reacción sigue una cinética de primer orden.

# ****2\. Inhibición catalítica****

Además de los factores usuales que pueden afectar el valor de $k_m$ como la temperatura o el pH, también existe un conjunto de sustancias conocidas como inhibidores enzimaticos que reducen o bloquean la catálisis enzimática, evitando la formación de producto. Se separa la inhibición en 2 categorías

## ****Inhibición reversible****

El inhibidor enzimatico se une mediante un enlace no covalente y débil al sustrato o enzima, bloqueando la acción de la enzima. Debido al débil enlace, es posible retirar el inhibidor, revirtiendo el proceso. Existen 3 clases de inhibidores con acción reversible

* Inhibidor competitivo: Una sustancia muy similar al sustrato que también se une a los sitios activos de la enzima. Reduce la concentración efectiva de sustrato, requiriendo de un $[S]$ mayor para alcanzar la velocidad máxima de reacción. Aumenta el $k_m$ aparente. Se puede revertir aumentando la concentración de sustrato hasta desplazar el inhibidor.

* Inhibidor no competitivo: Se une a la enzima o el complejo sin ocupar sitios activos pero volviendolos inutilizables, reduce la velocidad máxima de la reacción.

* Inhibidor acompetitivo/mixto: Se une solo al complejo pero no por el sitio activo, bloquea la catálsisis. Reduce la velocidad máxima y disminuye el $k_m$ aparente.

## ****Inhibidor irreversible****

El inhibidor reacciona con algún grupo funcional de la enzima (por lo general el sitio activo) y forma un enlace covalente permanente, volviendola incapaz de catalizar la reacción. En su mayoría, los inhibidores irreversibles son sustancias altamente tóxicas para los organismos vivos. Aumenta el $k_m$ efectivo de forma similar al inhibidor competitivo.
