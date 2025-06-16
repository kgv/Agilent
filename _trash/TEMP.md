### Пошаговая инструкция по настройке поиска по библиотеке NIST:

На основании **Agilent MassHunter Workstation Unknowns Analysis Familiarization Guide**.

1.  **Откройте или создайте метод анализа.** В программе Unknowns Analysis выберите в меню **Метод > Редактировать** (Method > Edit). Откроется диалоговое окно настройки метода.

2.  **Перейдите на вкладку поиска по библиотеке.** В окне метода найдите и откройте вкладку **Library Search**.

3.  **Выберите библиотеку NIST.**
    *   Нажмите на кнопку **Change Library** (в русской версии может называться "Изменить библиотеку").
    *   В открывшемся окне перейдите в каталог, где установлена ваша библиотека NIST (например, **NIST11.L**), выберите её и нажмите **Открыть** (Open).
    *   Вы можете добавить несколько библиотек для одновременного поиска.

4.  **Настройте параметры поиска.** На той же вкладке **Library Search** вы можете задать критерии поиска для повышения точности идентификации:
    *   **Search criteria (Критерии поиска):** Здесь можно выбрать тип предварительного поиска (Pre-search type), например, **Standard** или **Fast**.
    *   **Match factor (Коэффициент совпадения):** Установите минимальный порог совпадения для идентификации.
    *   **Use RT Match (Использовать сопоставление ВУ):** Если у вас есть данные о времени удерживания (RT), можно активировать эту опцию для более точного поиска.

5.  **Сохраните метод и выполните анализ.** После настройки всех параметров сохраните метод и примените его к вашим данным. Программа выполнит поиск по указанной библиотеке NIST и отобразит результаты совпадений в таблице компонентов.

NIST

* The standard version of NIST (NIST23) is recommended for most users (except for Agilent ChemStation/MassHunter and Shimadzu GC/MS Solutions). It includes the NIST library formatted in NIST format, which is the native format understood by the NIST MS Search program, which integrates with a number of data systems (e.g. Varian Saturn, Thermo Xcalibur, Waters MassLynx version >= 4.0). GC/MS, LC/MS, and MS spectra from many data systems can also be imported indirectly into AMDIS (see above) and then library searched via the AMDIS-NIST MS Search program integration.

* The Agilent format version of NIST (NIST23AG) is recommended primarily for most Agilent ChemStation/MassHunter users. It includes everything in the standard version plus the NIST EI library formatted in the Agilent .L library format for library searching directly from Agilent software (e.g. Data Analysis PBM search).

* The Multiformat version of NIST (NIST23MF) is recommended for Shimadzu GCMSsolution users in particular. It includes everything in the standard and Agilent versions of NIST plus the following additional native formats: Shimadzu GCMSsolution, Waters MassLynx, and Thermo Spectral ID.

Таким образом, ключевым является правильная настройка метода анализа во вкладке **Library Search**, где вы указываете путь к файлу библиотеки NIST и задаете критерии поиска.

MSSEARCH\mainlib

```
d:\NIST23\MSSEARCH\mainlib\synonym.in6 d:\NIST23\MSSEARCH\mainlib\alnumna2.in6 d:\NIST23\MSSEARCH\mainlib\alnumnam.in6 d:\NIST23\MSSEARCH\mainlib\alphana2.in6 d:\NIST23\MSSEARCH\mainlib\alphanam.in6 d:\NIST23\MSSEARCH\mainlib\binsub d:\NIST23\MSSEARCH\mainlib\Cmb_U_base.sdb d:\NIST23\MSSEARCH\mainlib\Cmb_U_indx.sdb d:\NIST23\MSSEARCH\mainlib\contrib.db d:\NIST23\MSSEARCH\mainlib\contrib.in6 d:\NIST23\MSSEARCH\mainlib\Eval_base.sdb d:\NIST23\MSSEARCH\mainlib\exactmw.in6 d:\NIST23\MSSEARCH\mainlib\FITS d:\NIST23\MSSEARCH\mainlib\form.in6 d:\NIST23\MSSEARCH\mainlib\Hmlg_base.sdb d:\NIST23\MSSEARCH\mainlib\ichi.dat d:\NIST23\MSSEARCH\mainlib\ichi2.dat d:\NIST23\MSSEARCH\mainlib\ichihash.idx d:\NIST23\MSSEARCH\mainlib\ichihash2.idx d:\NIST23\MSSEARCH\mainlib\ichiid.idx d:\NIST23\MSSEARCH\mainlib\ichiid2.idx d:\NIST23\MSSEARCH\mainlib\inchikey.in6 d:\NIST23\MSSEARCH\mainlib\LIBSIGN.MSD d:\NIST23\MSSEARCH\mainlib\loss.db d:\NIST23\MSSEARCH\mainlib\loss.in6 d:\NIST23\MSSEARCH\mainlib\loss_am0.db d:\NIST23\MSSEARCH\mainlib\loss_am0.in6 d:\NIST23\MSSEARCH\mainlib\maxmass.db d:\NIST23\MSSEARCH\mainlib\maxmass.in6 d:\NIST23\MSSEARCH\mainlib\mw.in6 d:\NIST23\MSSEARCH\mainlib\namesfx2.db d:\NIST23\MSSEARCH\mainlib\namesort.asc d:\NIST23\MSSEARCH\mainlib\namesrt2.db d:\NIST23\MSSEARCH\mainlib\nist.db d:\NIST23\MSSEARCH\mainlib\nist.in6 d:\NIST23\MSSEARCH\mainlib\peak.db d:\NIST23\MSSEARCH\mainlib\peak.in6 d:\NIST23\MSSEARCH\mainlib\peak_am0.db d:\NIST23\MSSEARCH\mainlib\peak_am0.in6 d:\NIST23\MSSEARCH\mainlib\peak_am2.db d:\NIST23\MSSEARCH\mainlib\peak_am2.in6 d:\NIST23\MSSEARCH\mainlib\peak_em.db d:\NIST23\MSSEARCH\mainlib\peak_em.in6 d:\NIST23\MSSEARCH\mainlib\README d:\NIST23\MSSEARCH\mainlib\registry.in6 d:\NIST23\MSSEARCH\mainlib\registry2.in6 d:\NIST23\MSSEARCH\mainlib\ri.dat d:\NIST23\MSSEARCH\mainlib\ri.idx d:\NIST23\MSSEARCH\mainlib\riref.dat d:\NIST23\MSSEARCH\mainlib\riref.idx d:\NIST23\MSSEARCH\mainlib\rivalues.in6 d:\NIST23\MSSEARCH\mainlib\specno.in6 d:\NIST23\MSSEARCH\mainlib\stcas.in6 d:\NIST23\MSSEARCH\mainlib\struct.db d:\NIST23\MSSEARCH\mainlib\struct.in6 d:\NIST23\MSSEARCH\mainlib\subbin.in6 d:\NIST23\MSSEARCH\mainlib\SUBINFO d:\NIST23\MSSEARCH\mainlib\subsum d:\NIST23\MSSEARCH\mainlib\SUBTYPES.DAT d:\NIST23\MSSEARCH\mainlib\synonym.db
```

ConstantFlow(1mL÷min,60C,2C÷min).3.D
