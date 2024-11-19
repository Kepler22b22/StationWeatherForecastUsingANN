begin
    
    ;fin and fout need gave in linux

    f = addfile(fin1,"r")
    ;beijing zone
    ;lat = 40
    ;lon = 116
    ;China zone
    ;lat = 15:55
    ;lon = 70:140
    ;Northern hemisphere
    ;15:55 = 0:90
    ;70:140 = 0:359
    ;------------------------------------------------------
    ; upper pressure variables

    ; Var1, geopotential_height
    x1_1 = f->HGT_3_ISBL({200},{55:15},{70:140})
    x1_2 = f->HGT_3_ISBL({500},{55:15},{70:140})
    x1_3 = f->HGT_3_ISBL({700},{55:15},{70:140})
    x1_4 = f->HGT_3_ISBL({850},{55:15},{70:140})

    ; Var2, upper air_temperature
    x2_1 = f->TMP_3_ISBL({200},{55:15},{70:140})
    x2_2 = f->TMP_3_ISBL({500},{55:15},{70:140})
    x2_3 = f->TMP_3_ISBL({700},{55:15},{70:140})
    x2_4 = f->TMP_3_ISBL({850},{55:15},{70:140})

    ; Var3, vertical velocity
    x3_1 = f->V_VEL_3_ISBL({200},{55:15},{70:140})
    x3_2 = f->V_VEL_3_ISBL({500},{55:15},{70:140})
    x3_3 = f->V_VEL_3_ISBL({700},{55:15},{70:140})
    x3_4 = f->V_VEL_3_ISBL({850},{55:15},{70:140})

    ; Var4, relative_humidity
    x4_1 = f->R_H_3_ISBL({200},{55:15},{70:140})
    x4_2 = f->R_H_3_ISBL({500},{55:15},{70:140})
    x4_3 = f->R_H_3_ISBL({700},{55:15},{70:140})
    x4_4 = f->R_H_3_ISBL({850},{55:15},{70:140})

    ; Var5, Absolute vorticity
    x5_1 = f->ABS_V_3_ISBL({200},{55:15},{70:140})
    x5_2 = f->ABS_V_3_ISBL({500},{55:15},{70:140})
    x5_3 = f->ABS_V_3_ISBL({700},{55:15},{70:140})
    x5_4 = f->ABS_V_3_ISBL({850},{55:15},{70:140})

    ; Var6, U component of wind
    x6_1 = f->U_GRD_3_ISBL({200},{55:15},{70:140})
    x6_2 = f->U_GRD_3_ISBL({500},{55:15},{70:140})
    x6_3 = f->U_GRD_3_ISBL({700},{55:15},{70:140})
    x6_4 = f->U_GRD_3_ISBL({850},{55:15},{70:140})

    ; Var7, V component of wind
    x7_1 = f->V_GRD_3_ISBL({200},{55:15},{70:140})
    x7_2 = f->V_GRD_3_ISBL({500},{55:15},{70:140})
    x7_3 = f->V_GRD_3_ISBL({700},{55:15},{70:140})
    x7_4 = f->V_GRD_3_ISBL({850},{55:15},{70:140})

    ;-------------------------------------------------------
    ;surface 10meter variables

    ; Var8, 10meter U wind component
    x8 = f->U_GRD_3_HTGL({55:15},{70:140})

    ; Var9, 10meter V wind component
    x9 = f->V_GRD_3_HTGL({55:15},{70:140})
    ;-------------------------------------------------------
    ;surface 2meter variables

    ; Var10, 2meter temperature
    x10 = f->TMP_3_HTGL({55:15},{70:140})

    ; Var11, 2meter specific humidity
    x11 = f->SPF_H_3_HTGL({55:15},{70:140})
    
    ; Var12, 2meter relative humidity
    x12 = f->R_H_3_HTGL({55:15},{70:140})

    ; Var13, maximum temperature
    ;x13 = f->T_MAX_3_HTGL({55:15},{70:140})

    ; Var14, minimum temperature
    ;x14 = f->T_MIN_3_HTGL({55:15},{70:140})
    ;-------------------------------------------------------
    ;surface variables

    ; Var15, surface_air_pressure
    x15 = f->PRES_3_SFC({55:15},{70:140})

    ; Var16, surface_geopotential_height
    x16 = f->HGT_3_SFC({55:15},{70:140})

    ; Var17, surface_temperature
    x17 = f->TMP_3_SFC({55:15},{70:140})

    ;-------------------------------------------------------
    ;other variables

    ; Var18, entire atmosphere total cloud cover
    ;x18 = f->T_CDC_3_EATM_ave3h({55:15},{70:140})

    ; Var19, surface convective inhibition
    x19_1 = f->CIN_3_SFC({55:15},{70:140})

    ; Var19, 180meter convective inhibition
    x19_2 = f->CIN_3_SPDY({55:15},{70:140})

    ; Var20, surface convective available potential energy
    x20_1 = f->CAPE_3_SFC({55:15},{70:140})

    ; Var20, 180meter convective available potential energy
    x20_2 = f->CAPE_3_SPDY({55:15},{70:140})

    ; Var21, downward short wave flux
    ;x21_1 = f->DSWRF_3_SFC_ave3h({55:15},{70:140})

    ; Var21, downward long wave flux
    ;x21_2 = f->DLWRF_3_SFC_ave3h({55:15},{70:140})

    ; Var21, upward short wave flux
    ;x21_3 = f->USWRF_3_SFC_ave3h({55:15},{70:140})

    ; Var21, upward long wave flux
    ;x21_4 = f->ULWRF_3_SFC_ave3h({55:15},{70:140})

    ; Var22, entire atmosphere precipitable water
    ;x22 = f->P_WAT_3_EATM({55:15},{70:140})

    ; Var23, surface total precipitation
    ;x23 = f->A_PCP_3_SFC_acc3h({55:15},{70:140})

    ; Var24, Pressure reduced to MSL
    ;x24 = f->PRMSL_3_MSL({55:15},{70:140})
    ;-------------------------------------------------------
    ; Output

    system("rm -f "+fout1)
    fo = addfile(fout1,"c")
    fo->gh200     = x1_1
    fo->gh500     = x1_2
    fo->gh700     = x1_3
    fo->gh850     = x1_4
    fo->t200      = x2_1
    fo->t500      = x2_2
    fo->t700      = x2_3
    fo->t850      = x2_4
    fo->w200      = x3_1
    fo->w500      = x3_2
    fo->w700      = x3_3
    fo->w850      = x3_4
    fo->rh200     = x4_1
    fo->rh500     = x4_2
    fo->rh700     = x4_3
    fo->rh850     = x4_4
    fo->absv200   = x5_1
    fo->absv500   = x5_2
    fo->absv700   = x5_3
    fo->absv850   = x5_4
    fo->u200      = x6_1
    fo->u500      = x6_2
    fo->u700      = x6_3
    fo->u850      = x6_4
    fo->v200      = x7_1
    fo->v500      = x7_2
    fo->v700      = x7_3
    fo->v850      = x7_4

    fo->u10m      = x8
    fo->v10m      = x9
    fo->t2m       = x10
    fo->sh2m      = x11
    fo->rh2m      = x12
    ;fo->tmax      = x13
    ;fo->tmin      = x14
    fo->p_sfc     = x15
    fo->hgt_sfc   = x16
    fo->t_sfc     = x17
    ;fo->tcc       = x18
    fo->cin_sfc   = x19_1
    fo->cin_180   = x19_2
    fo->cape_sfc  = x20_1
    fo->cape_180  = x20_2
    ;fo->dswave    = x21_1
    ;fo->dlwave    = x21_2
    ;fo->uswave    = x21_3
    ;fo->ulwave    = x21_4
    ;fo->eatmprep  = x22
    ;fo->prep_sfc  = x23
    ;fo->msl       = x24

    fo@history    = "Yonglin Qu & Xinyu Wen, Peking Univ, June 2020, version3"
end

